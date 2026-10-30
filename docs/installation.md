# Installation and compatibility

Choose the path your platform supports. Lucky Kit provides text instructions and a self-contained skill package; it does not require a particular AI provider.

## Plain chat: no installation

Paste [SKILL.md](../skills/lucky-kit/SKILL.md) into your chat, followed by your request. Attach the file instead if your platform supports reading attachments. Use the [Getting Started template](../README.md#getting-started) to describe your project.

Supply source excerpts, references, and templates only when needed. Relative links inside `SKILL.md` are files in this repository; pasting the instructions does not upload those files. Provide a requested file's contents if the assistant cannot access it. A local path alone does not grant project access.

## Native skill installation

If your platform supports skill packages, copy the complete `skills/lucky-kit/` folder into its documented skills directory. Keep this structure intact:

```text
lucky-kit/
  SKILL.md
  references/
  assets/templates/
  agents/             Optional platform metadata
  LICENSE.txt
  NOTICE.md
  OUTPUT-LICENSE.md
```

Use the platform's documented discovery and invocation method. “Use Lucky Kit to plan this application” is a natural-language request, not a universal activation command. Check that the platform actually loads the skill; avoid multiple copies in overlapping discovery locations. Platforms without a skill loader can use the plain-chat method.

## Optional installers

Manual copying is sufficient. For repeatable installation, run either installer from the repository root and explicitly select your platform's skills directory.

Python 3.10+:

```sh
python scripts/install-skill.py --skills-root "/path/to/host/skills"
```

PowerShell 7:

```powershell
./scripts/install-skill.ps1 -SkillsRoot "/path/to/host/skills"
```

Replace the placeholder with a real directory. Both installers append `lucky-kit`; pass the parent skills directory, not the final package path. Use `python3` if that is your Python executable. Python or PowerShell is needed only for its installer, not to use the skill.

Both installers require an explicit destination and never select a global directory automatically.

### Codex: install only in a selected project

Use the selected project's `.agents/skills` directory. Run one of these commands from the Lucky Kit repository root, replacing the project path:

```powershell
./scripts/install-skill.ps1 -SkillsRoot "C:/path/to/project/.agents/skills"
```

```sh
python scripts/install-skill.py --skills-root "/path/to/project/.agents/skills"
```

The resulting package is `<project>/.agents/skills/lucky-kit/`. Repeat only for projects where you want Lucky Kit available. Keep it out of user-level skill directories and shared parent directories when you want project-only availability. See the [official Codex skill locations](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills).

## Updating an older Lucky Kit

Back up local customizations before updating. To overwrite differing package files, repeat the installation command with Python's `--update` or PowerShell's `-Update` flag. Both installers check ordinary file conflicts before copying and retain extra destination files; they are not transactional against disk failures or concurrent edits.

When an update removes or reorganizes package files, move the old `lucky-kit` folder to a backup outside the platform's scanned skill directories. Install the new package into the same original location, then deliberately reapply any customizations. Do not merge obsolete references back into the package.

Reload the platform if needed and confirm skill discovery. A successful copy does not prove that the platform loaded or executed the instructions.

## Compatibility and evidence

The core workflow uses text instructions without required APIs, vendor commands, or a model client. Native discovery, automatic invocation, progressive loading, file access, and context limits depend on the platform. Instruction portability does not guarantee equal results across models or support for every platform.

Previously recorded local checks cover package integrity and installer behavior on Windows. They do not establish native integration behavior, execution on other operating systems, or output quality. CI configuration alone does not prove a completed hosted run. See [contribution checks](../CONTRIBUTING.md#validate-what-changed) for what each validator covers and [design decisions](redesign.md) for workflow details.
