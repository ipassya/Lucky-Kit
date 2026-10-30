# Contributing to Lucky Kit

Help people make better product decisions and give coding agents clearer work. A useful contribution improves that outcome without forcing every project through the same stack, questionnaire, or document set.

Issues and pull requests are welcome in English or Indonesian. Keep the [English](README.md) and [Indonesian](README.id.md) READMEs aligned when changing capabilities, installation, or licensing.

## Start with a concrete problem

Describe where the current workflow fails, the expected result, and the smallest example that demonstrates the difference. Good contributions include clearer instructions, better templates, accurate translations, installer fixes, and verified support for another host.

Discuss substantial workflows or integrations before building them. Focused corrections can go straight to a pull request. Follow the [community guidelines](CODE_OF_CONDUCT.md); use [SECURITY.md](SECURITY.md) for sensitive reports.

## Edit the canonical source

The installable package lives in `skills/lucky-kit/`. Put shared guidance in `SKILL.md`, conditional workflow detail in `references/`, and output templates in `assets/templates/`. Keep each rule at its natural source and link to it where needed.

Use descriptive lowercase kebab-case filenames, preserving conventional names such as `SKILL.md` and `LICENSE`. Keep generated applications, transcripts, and temporary test artifacts outside the repository.

Write workflow instructions and templates in English. Indonesian user instructions produce Indonesian output; other languages produce English output. Write for the reader's next decision. Prefer observable behavior and concrete examples to broad claims. Templates should prompt useful content without becoming copies of the workflow manual.

## Validate what changed

From the repository root:

```sh
python scripts/validate.py
python scripts/test-install.py
pwsh -File scripts/test-install.ps1
```

The package validator requires Python 3.10+ and uses only the standard library. It checks identity, licensing, local Markdown destinations, and links that would escape the installed package. OpenAI UI metadata is checked when present, not required by the core. It excludes template links that describe future application files. It does not validate remote sites or generated output quality.

Installer tests use Python 3.10+ or PowerShell 7 for their respective installers. They run in isolated temporary directories and check installation, repeatability, conflict handling, explicit updates, preservation of unrelated files, and invalid destinations. They do not modify your installed skill. Local Windows results do not establish macOS or Linux execution.

Skill changes also require the `quick_validate.py` supplied by skill-creator. Resolve its path in your environment and run it against `skills/lucky-kit`. This tool is not vendored here.

For workflow changes, exercise a representative request. Report the prompt, agent/model or review method, relevant environment, expected behavior, observed behavior, and limitations. Label self-review accurately. A spelling correction does not require an application demo.

After validation, use either installer at the destination originally chosen. For structural changes that remove files, use the backup-and-replace procedure in the [installation guide](docs/installation.md); ordinary update flags retain extra files.

## Make the result reviewable

A pull request should explain the user-visible problem, resulting behavior, checks actually run, and remaining limitations. Keep changes focused. Do not claim successful tests, compatibility, or performance without evidence.

AI-assisted contributions are welcome. State the tool and how it helped. You remain responsible for understanding the change, checking provenance, and validating the result.

## Rights and credit

By intentionally submitting a contribution for inclusion, you offer it under Lucky Kit's [GPLv3-only license](LICENSE). For your contributions to material used in generated project output, you also grant the [generated-output permission](skills/lucky-kit/OUTPUT-LICENSE.md). You retain your copyright; no copyright assignment is requested.

Only submit material you have the right to license on those terms. Identify third-party material separately with its source, revision, license, notices, and modifications. Public availability does not establish permission to reuse it, and the output permission does not override third-party rights.

Credit accepted contributions in pull requests and release notes. Preserve required notices with the covered material; record conceptual influences in [CREDITS.md](CREDITS.md).
