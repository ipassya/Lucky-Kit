# Distribution and release preparation

This guide records the project's distribution decisions and release checks. Published versions and downloadable packages are listed on [GitHub Releases](https://github.com/ipassya/Lucky-Kit/releases). This guide is not an external review or certification.

## Project identity

| Item | Decision |
| --- | --- |
| Display name | Lucky Kit |
| Skill identifier and package folder | `lucky-kit` |
| Creator and maintainer | Ihza Luckyan Passya |
| Purpose | Align app ideas, existing artifacts, and codebases into documentation and implementation handoffs. |
| Public documentation | English, with an equivalent Indonesian README. |
| Source license | GPL-3.0-only. |
| Generated output | Covered by the packaged additional permission where applicable. |
| Distribution in this source tree | Self-contained skill folder and local installer. |

The source folder is named `Lucky-Kit`; the installable package remains `lucky-kit`. Reading, installing, and validating the package does not require Git history or a configured remote.

## Package boundaries

`skills/lucky-kit/` is the independently installable unit. It carries instructions, references, templates, UI metadata, and legal notices. Community documents and repository scripts support maintenance; they are not loaded as skill instructions.

Keep the entrypoint focused and load detailed references as needed. Generated applications belong in their own workspaces. Avoid adding host-specific services or dependencies without a concrete workflow that needs them.

The [installation guide](installation.md) covers manual installation, plain chat, optional Python/PowerShell installers, and host discovery. Package validation and installer checks do not prove native skill loading on every platform.

## Authorship and reuse

Use “Created and maintained by Ihza Luckyan Passya” in public project documentation. Preserve copyright notices in distributed source. The [generated-output permission](../skills/lucky-kit/OUTPUT-LICENSE.md) does not require branding in users' applications.

Contributors retain authorship under the terms in [CONTRIBUTING.md](../CONTRIBUTING.md). Credit accepted work through real contributions and release notes. Do not infer endorsement from a reference or tool.

[CREDITS.md](../CREDITS.md) records conceptual influences. Imported code, templates, artwork, or substantial text require their own provenance, license, notices, and modification records. A courtesy link alone is not a substitute.

## License files

The canonical terms are in [LICENSE](../LICENSE). The package carries an identical `LICENSE.txt`, a notice, and the additional generated-output permission. Preserve their scope when editing surrounding documentation.

The output permission covers eligible Lucky Kit material incorporated into project-specific output. It does not relicense Lucky Kit itself, a redistributed reusable template library, or third-party material. Consult the actual license files for the terms.

## Before public release

| Work | Required result |
| --- | --- |
| Public destination | A real owner/repository URL and verified documentation links. |
| Private reporting | Working security and moderation channels, documented and checked. |
| Provenance | Sources, applicable licenses, and notices reviewed for imported material. |
| Package checks | Package validator and skill-creator validator pass on the release source. |
| Installer checks | Clean install, repeat install, conflict rejection, and update checks pass. |
| Hosted CI | A real successful workflow run, distinct from local results. |
| Workflow evidence | An idea-to-handoff interaction in each advertised language, with model, environment, outputs, and limitations recorded. |
| Release artifact | A versioned source snapshot and archive containing the complete skill and legal notices. |

Keep raw test artifacts outside the source tree. Curated examples or walkthroughs must come from actual runs, with private information removed and simulated content labeled.

Plugin distribution requires separate packaging and validation before it is advertised. Badges, screenshots, release links, and usage claims should point to real evidence. A website or visual identity can follow when it has a clear purpose.

## Describe readiness accurately

Local package checks establish structural integrity within their scope. They do not prove agent behavior, cross-host compatibility, security certification, or production readiness of generated applications.

Publish only after the relevant release work is complete and publication has been requested. Keep unresolved items visible rather than turning planned work into claims.
