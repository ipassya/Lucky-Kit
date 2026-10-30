---
name: lucky-kit
description: Turn app ideas, existing specifications, or codebases into aligned documentation and implementation handoffs. Use for app planning with focused discovery and workspace documents, reconciling requirements and design systems, documenting existing behavior, or reviewing readiness. Not for routine code edits.
license: GPL-3.0-only; generated-output permission in OUTPUT-LICENSE.md
metadata:
  author: Ihza Luckyan Passya
---

# Lucky Kit

Produce the smallest useful specification for the requested outcome. Start from the user's idea, artifacts, or code; reuse existing answers.

## Rules

- Use Indonesian for discussion and generated documents when the user's main instruction is Indonesian; otherwise use English. Translate template prose and headings; preserve identifiers and established names.
- Preserve scope, constraints, accepted choices, and project conventions. Explain material conflicts before replacing decisions. Guide beginners with concrete scenarios; let professionals supply decisions directly.
- For planning, actively probe consequential needs, assumptions, and trade-offs using [planning](references/planning.md). Reuse known answers; do not limit discovery to immediate blockers. Separate observed behavior, explicit decisions, assumptions, proposals, and unknowns.
- App planning or specification requests authorize creating and maintaining documents in the application's workspace without a separate save request. Reuse an unambiguous application workspace from context; if missing or ambiguous, establish it before writing and continue discovery meanwhile. Never put application output inside Lucky Kit. Explicit chat-only, discussion-only, and review-only requests stay in chat unless edits are requested. Documentation does not authorize code changes, deployment, or purchases.

## Route by need

Read only the reference needed for the current action:

| Need | Reference |
| --- | --- |
| Product, stack, or design decisions | [Planning](references/planning.md) |
| Existing or conflicting PRDs, design systems, backlogs | [Alignment](references/alignment.md) |
| Documentation from implementation | [Codebase](references/codebase.md) |
| Specifications, tasks, or handoffs | [Documents](references/documents.md) |

These are entry points, not mandatory phases. Small requests need only this core. For app planning, save a useful draft once the workspace and basic outcome are known; do not wait for the entire interview to finish. Choose the smallest useful file set with [documents](references/documents.md): reuse an existing owner, add a section, or create a separate document only for a concrete user need. PRD, TRD, AFD, DBD, BSD, and IPD are available formats, not a checklist. Cover the requested scope fully; templates and formal registers are optional.

## Keep work connected

Search relevant sources before asking. Read affected sections, broadening for required coverage; reuse findings. Give each rule one canonical owner and link dependents. Preserve existing IDs and paths. Update changed sections and affected dependents instead of regenerating everything.

Check relevant scope, flows, design, data, acceptance, and tasks for contradictions. Remove empty scaffolding. Report outputs, material gaps, and the next action. Keep approval, readiness, implementation, and verification separate. Code does not prove intent; unrun tests do not prove success.

## Create, revise, and finish responsibly

Before writing, inspect applicable workspace instructions, existing content, and the affected sources. Make the smallest coherent change that serves the user's requested outcome. Apply relevant domain practices, such as access rules for shared data or recovery paths for irreversible actions, rather than imposing an unrelated checklist. Verify consequential external claims against current primary sources when available; label proposals and uncertainty. Never replace established choices merely to follow a fashionable practice.

After writing, review the actual diff or changed sections, update affected dependents, and check relevant links, acceptance, and evidence. Run required workspace checks and checks justified by the change; a prose edit does not automatically require application tests. Resolve findings within scope, report checks that could not run, and stop after sufficient verification.

In an existing Git repository, automatically commit the completed, validated changes for this task unless the user or workspace instructions say otherwise. Inspect the working tree and staged diff first; include only this task's changes and preserve unrelated work. If mixed or pre-staged changes cannot be isolated safely, do not bundle, discard, or unstage them; report why the commit is blocked. Commit a coherent update, not every draft write. Do not create an empty commit, initialize Git, push, rewrite history, or bypass failed checks. Without Git, save normally and report that no commit was made. Report the actual commit hash or the reason it remains uncommitted.

## Adapt to capabilities

No vendor, API, named tool, or runtime is required. Without file-writing access, return usable document content with intended filenames and say it has not been saved. In plain chat, use pasted input. If files, links, images, or references are inaccessible, disclose that and request the smallest relevant excerpt. Missing optional references do not block basic work.

Use available tools when helpful. Verify changing external facts from primary sources when possible; otherwise mark them unverified. Partial evidence supports only a partial assessment. Never invent research, business intent, execution results, or compatibility. No Lucky Kit branding is required in generated applications.
