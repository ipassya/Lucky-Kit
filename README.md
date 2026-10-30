# Lucky Kit

[![CI](https://github.com/ipassya/Lucky-Kit/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/ipassya/Lucky-Kit/actions/workflows/validate.yml)
[![Release](https://img.shields.io/github/v/release/ipassya/Lucky-Kit?label=release)](https://github.com/ipassya/Lucky-Kit/releases/latest)

**Turn an app idea, existing documents, or a codebase into a clear plan for implementation.**

[Bahasa Indonesia](README.id.md) · [Installation](docs/installation.md) · [Download v1.0.0 (ZIP)](https://github.com/ipassya/Lucky-Kit/releases/download/v1.0.0/lucky-kit-v1.0.0.zip) · [Contributing](CONTRIBUTING.md)

Lucky Kit is a reusable set of AI instructions for product planning and documentation. It helps founders, product teams, and developers connect requirements, user flows, design, data, and implementation tasks. Start with what you know; unresolved decisions stay visible.

## What you get

| Your starting point | Useful output |
| --- | --- |
| An idea | Guided discovery and saved planning documents with scope, key flows, constraints, and open decisions |
| Existing documents | Aligned requirements and design, with conflicts identified and resolved |
| A working codebase | Documentation of observed behavior, with evidence and coverage limits |
| Ready specifications | An implementation handoff with tasks, dependencies, and acceptance criteria |

App planning automatically creates and updates documents in your application's workspace once the destination and basic outcome are known. You do not need to ask separately to save them. If the destination is unclear, Lucky Kit asks for it while continuing discovery. Explicit discussion-only and review-only requests stay in chat; without file access, it returns document content and clearly states that it has not been saved. Reviewing or documenting an application does not authorize code changes.

Lucky Kit includes a probing interview in the spirit of grill-me, usually one question at a time. It explores concrete scenarios, challenges assumptions, follows answers into their consequences, and accepts answers beyond its suggested options. It reuses known answers and updates drafts as decisions emerge. You can ask it to stop questions and produce a draft with explicit unknowns; no separate interview skill is required.

Lucky Kit chooses files by who will use them and what decision or work they support. It updates an existing document or adds a section before creating a separate file. PRD (Product Requirement Documentation), TRD (Technical Requirement Documentation), AFD (App Flow Documentation), DBD (Design Brief Documentation), BSD (Backend Schema Documentation), and IPD (Implementation Plan Documentation) are available formats, not a required package. Even a complex app can use fewer than six files; a focused schema or handoff request does not automatically add companion documents.

Depth follows the next use: exploration captures needs and consequential questions, decision support compares meaningful trade-offs, and an implementation handoff provides the contracts and acceptance needed to act. Lucky Kit infers this from your request, deepens existing documents as decisions mature, and does not impose a word count or a mode-selection questionnaire.

For each creation or revision, Lucky Kit follows workspace conventions, preserves authoritative decisions, reviews affected content and dependents, and performs checks appropriate to the change. In an existing Git repository, it automatically commits a coherent, validated task update unless you or the workspace instruct otherwise. It preserves unrelated work and reports blockers rather than bundling mixed changes. It does not initialize Git or push automatically. Without Git, it saves the documents and reports that no commit was made.

Changes mixed in the same file require hunk-level isolation; selecting the whole file is not sufficient. Failed hooks remain enabled, and explicit no-commit requests leave task edits uncommitted and unstaged. A commit is reported only after its actual contents are verified.

## Getting started

1. Paste [SKILL.md](skills/lucky-kit/SKILL.md) into your AI chat, or attach it if file reading is supported.
2. Copy the template below. Replace the brackets; use **“undecided”** where needed.
3. Send it with relevant material and your application's workspace. Supply referenced files when requested; planning documents are saved there when file access is available.

### Copy this template

```text
Use Lucky Kit to plan [app] for [users], solving [problem].
Main flow: [trigger → actions → outcome].
MVP: [essential features]. Out of scope: [exclusions].
Platform and design: [web/mobile/other; visual needs or existing design system].
Data and integrations: [records, sources, access rules, external services].
Constraints: [budget, timeline, stack, or other requirements].
Existing material: [none, documents, designs, or code; locations if accessible].
Deliver: [brief, aligned specifications, current-state docs, or handoff].
Application workspace: [destination; or explicitly request chat-only discussion].
Reuse existing decisions, probe consequential gaps and trade-offs, and keep documents
  updated as answers emerge.
```

### Example: personal finance app

```text
Use Lucky Kit to plan a personal finance app for freelancers who need to track irregular
  income.
Main flow: add income or expense → update wallet balance → review the monthly budget.
MVP: manual transactions, wallets, categories, monthly budgets. Out of scope: bank sync,
  payments, investments.
Platform and design: mobile-friendly web; a simple dashboard and quick transaction
  entry.
Data and integrations: private per-user records in IDR; email sign-in; no bank
  connection.
Constraints: 6-week MVP, hosting up to IDR 500,000/month; stack undecided.
Existing material: idea only.
Application workspace: [path to my personal finance app workspace].
Deliver: saved planning documents with scope, flows, data needs, acceptance criteria,
  and open decisions; split into specialized documents where needed.
Reuse existing decisions, probe consequential gaps and trade-offs, and keep documents
  updated as answers emerge.
```

Replace the example's domain, users, and constraints to plan another idea. Indonesian requests produce Indonesian discussion and documents; other languages produce English output.

## Use it with your tools

| Environment | How to start |
| --- | --- |
| AI chat | Paste the instructions and your request; provide relevant source excerpts as needed. |
| Assistant with project access | Provide the instructions and project location: “Document this app's implemented flows and data model; distinguish evidence from proposals.” |
| Agent with skill support | Install the complete `skills/lucky-kit/` folder using the host's supported location, then ask it to use Lucky Kit. |

The text instructions are portable; native skill loading and file access depend on your platform. A local path alone does not give a chat access to your files. Output quality depends on the model and available context.

Manual copying is sufficient for installation. Optional Python and PowerShell installers, updates, and verification limits are covered in the [installation guide](docs/installation.md). The skill itself needs no runtime or service account.

## Resources

- [Contribution guide](CONTRIBUTING.md): package structure, editing, and required checks.
- [Design decisions](docs/redesign.md): workflow structure and context measurement.
- [Behavior evaluation](docs/behavior-evaluation.md): reproducible isolated scenarios, Git evidence, and human review of discovery and document usefulness.
- [Community guidelines](CODE_OF_CONDUCT.md) · [Security reporting](SECURITY.md) · [Release preparation](docs/open-source.md).

## License and credits

Created and maintained by **Ihza Luckyan Passya**. Copyright © 2026.

Licensed under [GPL-3.0-only](LICENSE), with a [generated-output permission](skills/lucky-kit/OUTPUT-LICENSE.md) for eligible material used in project-specific output, including private and commercial work. Generated applications do not require Lucky Kit branding. Redistribution of the skill or reusable template library remains subject to the applicable terms. See [credits](CREDITS.md).
