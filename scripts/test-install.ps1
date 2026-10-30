#Requires -Version 7.0
# Copyright (C) 2026 Ihza Luckyan Passya
# SPDX-License-Identifier: GPL-3.0-only
$ErrorActionPreference = 'Stop'
$installer = Join-Path $PSScriptRoot 'install-skill.ps1'
$source = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../skills/lucky-kit'))
$temporaryParent = [IO.Path]::GetFullPath([IO.Path]::GetTempPath())
$testDirectory = Join-Path $temporaryParent ('lucky-kit-install-test-' + [guid]::NewGuid().ToString('N'))
$target = Join-Path $testDirectory 'lucky-kit'

function Assert-Condition([bool]$Condition, [string]$Message) {
    if (-not $Condition) { throw $Message }
}

function Get-Inventory([string]$Directory) {
    $inventory = @{}
    foreach ($file in Get-ChildItem -LiteralPath $Directory -File -Recurse) {
        $relative = $file.FullName.Substring($Directory.Length).TrimStart([char[]]'\/')
        $inventory[$relative] = (Get-FileHash -LiteralPath $file.FullName -Algorithm SHA256).Hash
    }
    return $inventory
}

function Assert-MatchesSource {
    $expected = Get-Inventory $source
    $actual = Get-Inventory $target
    foreach ($key in $expected.Keys) {
        Assert-Condition ($actual[$key] -eq $expected[$key]) "Installed file differs: $key"
    }
}

try {
    New-Item -ItemType Directory -Path $testDirectory | Out-Null
    foreach ($arguments in @(@{}, @{ SkillsRoot = '' }, @{ SkillsRoot = '   ' })) {
        $rejected = $false
        try {
            & {
                # Prevent a regression from writing to a real global skill directory.
                function New-Item { throw 'Unexpected write without an explicit skills root.' }
                function Copy-Item { throw 'Unexpected write without an explicit skills root.' }
                & $installer @arguments | Out-Null
            }
        }
        catch {
            if ($_.Exception.Message -notmatch 'Specify -SkillsRoot explicitly') { throw }
            $rejected = $true
        }
        Assert-Condition $rejected 'Missing, empty, and whitespace-only roots must be rejected.'
    }
    & $installer -SkillsRoot $testDirectory | Out-Null
    Assert-MatchesSource
    foreach ($notice in @('LICENSE.txt', 'NOTICE.md', 'OUTPUT-LICENSE.md')) {
        Assert-Condition (Test-Path -LiteralPath (Join-Path $target $notice) -PathType Leaf) "Missing legal file: $notice"
    }

    $repeat = (& $installer -SkillsRoot $testDirectory) -join "`n"
    Assert-Condition ($repeat -match 'Already up to date') 'Repeated install should make no copies.'

    $extra = Join-Path $target 'local-note.txt'
    Set-Content -LiteralPath $extra -Value 'Keep this local note.'
    Add-Content -LiteralPath (Join-Path $target 'SKILL.md') -Value 'Local customization.'
    Remove-Item -LiteralPath (Join-Path $target 'agents/openai.yaml')
    $before = Get-Inventory $target
    $rejected = $false
    try { & $installer -SkillsRoot $testDirectory | Out-Null }
    catch {
        if ($_.Exception.Message -notmatch 'Installed files differ') { throw }
        $rejected = $true
    }
    Assert-Condition $rejected 'Conflicting files must require -Update.'
    $after = Get-Inventory $target
    Assert-Condition ($before.Count -eq $after.Count) 'Rejected install partially copied files.'
    foreach ($key in $before.Keys) {
        Assert-Condition ($before[$key] -eq $after[$key]) "Rejected install changed $key"
    }

    & $installer -SkillsRoot $testDirectory -Update | Out-Null
    Assert-MatchesSource
    Assert-Condition ((Get-Content -LiteralPath $extra -Raw).Trim() -eq 'Keep this local note.') 'Update removed an extra local file.'

    $rejected = $false
    try { & $installer -SkillsRoot (Split-Path -Parent $source) -Update | Out-Null }
    catch {
        if ($_.Exception.Message -notmatch 'Source and destination must be different') { throw }
        $rejected = $true
    }
    Assert-Condition $rejected 'Installer must refuse its source directory as a destination.'

    $rejected = $false
    try { & $installer -SkillsRoot (Join-Path $source 'nested') -Update | Out-Null }
    catch {
        if ($_.Exception.Message -notmatch 'must not overlap') { throw }
        $rejected = $true
    }
    Assert-Condition $rejected 'Installer must refuse a destination inside its source.'
    Assert-Condition (-not (Test-Path -LiteralPath (Join-Path $source 'nested'))) 'Overlap rejection wrote to the source.'

    $blockedRoot = Join-Path $testDirectory 'blocked'
    $blockedTarget = Join-Path $blockedRoot 'lucky-kit'
    New-Item -ItemType Directory -Path $blockedTarget | Out-Null
    Set-Content -LiteralPath (Join-Path $blockedTarget 'agents') -Value 'A file blocks the required directory.'
    $before = Get-Inventory $blockedTarget
    $rejected = $false
    try { & $installer -SkillsRoot $blockedRoot -Update | Out-Null }
    catch {
        if ($_.Exception.Message -notmatch 'Destination parent is not a directory') { throw }
        $rejected = $true
    }
    Assert-Condition $rejected 'A parent-file collision must reject the install.'
    $after = Get-Inventory $blockedTarget
    Assert-Condition ($before.Count -eq $after.Count) 'Parent collision caused a partial installation.'
    foreach ($key in $before.Keys) {
        Assert-Condition ($before[$key] -eq $after[$key]) "Parent collision changed $key"
    }

    Write-Output 'PASS: explicit destination required, clean and repeat installs, legal notices, conflict rejection without partial writes, explicit update, extra-file preservation, self-install and overlap rejection, and parent-file collision rejection.'
}
finally {
    if (Test-Path -LiteralPath $testDirectory) {
        $resolvedTest = (Resolve-Path -LiteralPath $testDirectory).Path
        $allowedParent = (Resolve-Path -LiteralPath $temporaryParent).Path.TrimEnd([char[]]'\/') + [IO.Path]::DirectorySeparatorChar
        if (-not $resolvedTest.StartsWith($allowedParent, [StringComparison]::OrdinalIgnoreCase) -or
            (Split-Path -Leaf $resolvedTest) -notlike 'lucky-kit-install-test-*') {
            throw 'Refusing cleanup outside the test temporary directory.'
        }
        $items = @((Get-Item -LiteralPath $resolvedTest -Force)) + @(Get-ChildItem -LiteralPath $resolvedTest -Force -Recurse)
        if (@($items | Where-Object { $_.Attributes -band [IO.FileAttributes]::ReparsePoint }).Count -gt 0) {
            throw 'Refusing cleanup of a test directory containing links.'
        }
        Remove-Item -LiteralPath $resolvedTest -Recurse -Force
    }
}
