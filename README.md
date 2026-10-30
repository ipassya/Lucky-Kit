# Lucky Kit

**Turn an app idea, existing documents, or a codebase into a clear plan for implementation.**

[Bahasa Indonesia](README.id.md) · [Installation](docs/installation.md) · [Contributing](CONTRIBUTING.md)

Lucky Kit is a reusable set of AI instructions for product planning and documentation. It helps founders, product teams, and developers connect requirements, user flows, design, data, and implementation tasks. Start with what you know; unresolved decisions stay visible.

## What you get

| Your starting point | Useful output |
| --- | --- |
| An idea | A project brief with scope, key flows, constraints, and open decisions |
| Existing documents | Aligned requirements and design, with conflicts identified and resolved |
| A working codebase | Documentation of observed behavior, with evidence and coverage limits |
| Ready specifications | An implementation handoff with tasks, dependencies, and acceptance criteria |

Small projects start with one brief. Separate product, flow, design, technical, data, and delivery documents are added when needed. Reviewing or documenting an application does not authorize code changes.

## Getting started

1. Paste [SKILL.md](skills/lucky-kit/SKILL.md) into your AI chat, or attach it if file reading is supported.
2. Copy the template below. Replace the brackets; use **“undecided”** where needed.
3. Send it with any relevant material. Supply referenced files when requested; save outputs in your application's workspace.

### Copy this template

```text
Use Lucky Kit to plan [app] for [users], solving [problem].
Main flow: [trigger → actions → outcome].
MVP: [essential features]. Out of scope: [exclusions].
Platform and design: [web/mobile/other; visual needs or existing design system].
Data and integrations: [records, sources, access rules, external services].
Constraints: [budget, timeline, stack, or other requirements].
Existing material: [none, documents, designs, or code; locations if accessible].
Deliver: [brief, aligned specifications, current-state docs, or handoff]; [chat or destination].
Reuse existing decisions, flag gaps, and ask only questions that block progress.
```

### Example: personal finance app

```text
Use Lucky Kit to plan a personal finance app for freelancers who need to track irregular income.
Main flow: add income or expense → update wallet balance → review the monthly budget.
MVP: manual transactions, wallets, categories, monthly budgets. Out of scope: bank sync, payments, investments.
Platform and design: mobile-friendly web; a simple dashboard and quick transaction entry.
Data and integrations: private per-user records in IDR; email sign-in; no bank connection.
Constraints: 6-week MVP, hosting up to IDR 500,000/month; stack undecided.
Existing material: idea only.
Deliver: a brief in chat with scope, flows, data needs, acceptance criteria, and open decisions.
Reuse existing decisions, flag gaps, and ask only questions that block progress.
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
- [Community guidelines](CODE_OF_CONDUCT.md) · [Security reporting](SECURITY.md) · [Release preparation](docs/open-source.md).

## License and credits

Created and maintained by **Ihza Luckyan Passya**. Copyright © 2026.

Licensed under [GPL-3.0-only](LICENSE), with a [generated-output permission](skills/lucky-kit/OUTPUT-LICENSE.md) for eligible material used in project-specific output, including private and commercial work. Generated applications do not require Lucky Kit branding. Redistribution of the skill or reusable template library remains subject to the applicable terms. See [credits](CREDITS.md).
