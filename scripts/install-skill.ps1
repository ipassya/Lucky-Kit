#Requires -Version 7.0
# Copyright (C) 2026 Ihza Luckyan Passya
# SPDX-License-Identifier: GPL-3.0-only
[CmdletBinding()]
param(
    [string]$SkillsRoot,
    [switch]$Update
)

$ErrorActionPreference = 'Stop'
$sourceDirectory = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../skills/lucky-kit'))

if ([string]::IsNullOrWhiteSpace($SkillsRoot)) {
    throw 'Specify -SkillsRoot explicitly. For a Codex project, use <project>/.agents/skills. No global installation is selected automatically.'
}

$destinationDirectory = [IO.Path]::GetFullPath((Join-Path $SkillsRoot 'lucky-kit'))
if ($sourceDirectory -eq $destinationDirectory) {
    throw 'Source and destination must be different directories.'
}
$sourcePrefix = $sourceDirectory.TrimEnd([char[]]'\/') + [IO.Path]::DirectorySeparatorChar
$destinationPrefix = $destinationDirectory.TrimEnd([char[]]'\/') + [IO.Path]::DirectorySeparatorChar
if ($destinationPrefix.StartsWith($sourcePrefix, [StringComparison]::OrdinalIgnoreCase) -or
    $sourcePrefix.StartsWith($destinationPrefix, [StringComparison]::OrdinalIgnoreCase)) {
    throw 'Source and destination must not overlap.'
}
if (-not (Test-Path -LiteralPath (Join-Path $sourceDirectory 'SKILL.md') -PathType Leaf)) {
    throw "Skill source not found: $sourceDirectory"
}

# Check every collision before writing, so a rejected update leaves files untouched.
$pendingCopies = @()
$conflicts = @()
foreach ($sourceFile in (Get-ChildItem -LiteralPath $sourceDirectory -File -Recurse)) {
    $relativePath = $sourceFile.FullName.Substring($sourceDirectory.Length).TrimStart([char[]]'\/')
    $targetPath = Join-Path $destinationDirectory $relativePath
    # Check directory collisions before any copy, including missing parent trees.
    $ancestor = Split-Path -Parent $targetPath
    while ($ancestor) {
        if (Test-Path -LiteralPath $ancestor) {
            if (-not (Test-Path -LiteralPath $ancestor -PathType Container)) {
                throw "Destination parent is not a directory: $ancestor"
            }
            break
        }
        $ancestor = Split-Path -Parent $ancestor
    }
    if (Test-Path -LiteralPath $targetPath) {
        if (-not (Test-Path -LiteralPath $targetPath -PathType Leaf)) {
            throw "Destination is not a file: $targetPath"
        }
        $sourceHash = (Get-FileHash -LiteralPath $sourceFile.FullName -Algorithm SHA256).Hash
        $targetHash = (Get-FileHash -LiteralPath $targetPath -Algorithm SHA256).Hash
        if ($sourceHash -eq $targetHash) { continue }
        $conflicts += $relativePath
    }
    $pendingCopies += [PSCustomObject]@{ Source = $sourceFile.FullName; Target = $targetPath }
}

if ($conflicts.Count -gt 0 -and -not $Update) {
    throw "Installed files differ: $($conflicts -join ', '). Review them, then use -Update to overwrite matching paths."
}

foreach ($copy in $pendingCopies) {
    $parentDirectory = Split-Path -Parent $copy.Target
    New-Item -ItemType Directory -Path $parentDirectory -Force | Out-Null
    Copy-Item -LiteralPath $copy.Source -Destination $copy.Target -Force
}

if ($pendingCopies.Count -eq 0) {
    Write-Output "Already up to date: Lucky Kit at $destinationDirectory"
} else {
    Write-Output "Installed Lucky Kit ($($pendingCopies.Count) files): $destinationDirectory"
}
Write-Output 'Extra destination files are retained. Use your host skill invocation or plain chat; reload the host if the update is not visible.'
