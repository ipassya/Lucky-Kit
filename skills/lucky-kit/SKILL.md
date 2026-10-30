---
name: lucky-kit
description: Turn app ideas, existing specifications, or codebases into aligned documentation and implementation handoffs. Use for planning, reconciling requirements and design systems, documenting existing behavior, or reviewing readiness. Not for routine code edits.
license: GPL-3.0-only; generated-output permission in OUTPUT-LICENSE.md
metadata:
  author: Ihza Luckyan Passya
---

# Lucky Kit

Produce the smallest useful specification for the requested outcome. Start from the user's idea, artifacts, or code; reuse existing answers.

## Rules

- Use Indonesian for discussion and generated documents when the user's main instruction is Indonesian; otherwise use English. Translate template prose and headings; preserve identifiers and established names.
- Preserve scope, constraints, accepted choices, and project conventions. Explain material conflicts before replacing decisions. Guide beginners with concrete scenarios; let professionals supply decisions directly.
- Ask only questions that materially block the result. State reversible assumptions and continue independent work. Separate observed behavior, explicit decisions, assumptions, proposals, and unknowns.
- Discussion/review stays in chat unless saving/editing is requested. Write files in the application's workspace, outside Lucky Kit. Resolve an ambiguous destination first. Documentation does not authorize code changes, deployment, or purchases.

## Route by need

Read only the reference needed for the current action:

| Need | Reference |
| --- | --- |
| Product, stack, or design decisions | [Planning](references/planning.md) |
| Existing or conflicting PRDs, design systems, backlogs | [Alignment](references/alignment.md) |
| Documentation from implementation | [Codebase](references/codebase.md) |
| Specifications, tasks, or handoffs | [Documents](references/documents.md) |

These are entry points, not mandatory phases. Small requests need only this core. Start with one brief unless the request or complexity warrants separate documents. Cover the requested scope fully; templates and formal registers are optional.

## Keep work connected

Search relevant sources before asking. Read affected sections, broadening for required coverage; reuse findings. Give each rule one canonical owner and link dependents. Preserve existing IDs and paths. Update changed sections and affected dependents instead of regenerating everything.

Check relevant scope, flows, design, data, acceptance, and tasks for contradictions. Remove empty scaffolding. Report outputs, material gaps, and the next action. Keep approval, readiness, implementation, and verification separate. Code does not prove intent; unrun tests do not prove success.

## Adapt to capabilities

No vendor, API, named tool, or runtime is required. In plain chat, use pasted input and return usable document sections. If files, links, images, or references are inaccessible, disclose that and request the smallest relevant excerpt. Missing optional references do not block basic work.

Use available tools when helpful. Verify changing external facts from primary sources when possible; otherwise mark them unverified. Partial evidence supports only a partial assessment. Never invent research, business intent, execution results, or compatibility. No Lucky Kit branding is required in generated applications.
