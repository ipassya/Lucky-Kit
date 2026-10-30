# Choose and connect documents

Honor requested formats and existing paths. App planning produces saved Markdown documents by default once the application workspace is established, unless the user explicitly requests chat-only or discussion-only output. No separate permission to save is needed. Start with a useful draft, label unknowns, and revise it as discovery progresses. Do not overwrite an operational README with planning boilerplate.

For a new workspace without documentation conventions, `docs/project-brief.md` can start the plan or hold a small complete specification. It is not the default stopping point. Preserve equivalent existing documents instead of creating duplicates. Keep navigation in the existing entry point or brief when multiple documents need it; do not create a separate index for a single self-contained file.

## Match depth to the next use

Infer the reader's intended outcome from the request and available context. A new app idea defaults to implementation preparation, including relevant specifications and a milestone/task plan, even if the user does not name those artifacts. Explicit exploration, brief-only, decision support, review, or targeted-document requests keep their scope. These are levels of detail, not mandatory phases, modes to ask the user to select, or additional documents:

| Immediate need | Useful depth | Defer unless it changes the current decision |
| --- | --- | --- |
| Explicitly explore an idea or understand a problem | Concrete user scenario, desired outcome, bounded scope hypothesis, important constraints, and the next consequential questions | Stack selection, field-by-field schemas, exhaustive states, implementation tasks |
| Choose between approaches or settle a rule | Relevant alternatives, trade-offs under known constraints, a recommendation with its assumptions, and what the choice changes | Detailed implementation for every alternative or a full delivery package |
| Plan an app idea for implementation or prepare a full handoff | Relevant product, flow, design, technical, and data specifications; milestones and actionable tasks across the bounded first release; acceptance, verification, readiness, and blockers | Speculative future releases, unneeded architecture, and file-by-file plans for work not yet understood |

An exploratory draft can be short without losing known constraints. An implementation plan can be detailed without multiplying files. For a targeted correction or bounded handoff, update the affected rule and dependents at their established depth; do not expand unrelated sections. As decisions mature, deepen the same owner or split substantial topics according to the file-need criteria below. Explicit requests for comprehensive detail still govern.

Check usefulness, not a fixed page, word, section, or file count: can the intended reader take the next step, and does each substantive section help that step? Remove premature detail or duplication; retain detail necessary to prevent guessing about material behavior.

## Complete implementation preparation

For an app idea or full planning request, create the relevant documentation now rather than finishing with an offer to produce it in another turn. Use this completion test:

- The bounded release has users, scope, constraints, observable acceptance, and relevant success, rejection, and recovery behavior.
- Applicable design, technical, data, and interface decisions are concrete enough to guide work. Keep proposals and unresolved material decisions visibly separate from accepted requirements.
- The delivery plan covers every in-scope capability with dependency-ordered milestones and actionable tasks, including verification and release/operations work where relevant. Link tasks to their specification owners.
- The next implementable task has sufficient inputs and checks to proceed. If none is ready, identify the smallest unblocking action and the tasks it affects. Unknowns do not excuse omitting independent specifications or the rest of the plan.
- Navigation, shared contracts, acceptance, and task statuses agree. Report what is ready, what is conditional on proposals, and what remains blocked. A complete planning draft can contain blockers; it must not be called implementation-ready as a whole while material blockers remain.

## Decide whether a file is needed

Before creating or splitting a document, identify its reader, the decision or implementation work it supports, and why an existing section or document cannot serve that need well. This can be a brief explanation, not a new register or approval step. A feature mentioning data, screens, or delivery does not by itself require BSD, DBD, or IPD files.

Prefer updating the current owner when it remains usable. Create a separate file when explicitly requested or when substantial detail, a distinct audience/owner, or independent maintenance makes it materially more useful. Do not keep detailed flows, schemas, and delivery backlogs in an unreadable brief merely to avoid more files. If the need is only speculative or the file would mostly repeat content or list unknowns, retain relevant questions in the current draft and defer the separate file. Reassess when new answers or complexity justify a split; when splitting, move authoritative detail and link back instead of copying it.

Create documents justified by the current request now, without deferring useful coverage merely to minimize file count. Explain the selected file set briefly, including meaningful deferrals; do not recite six unnecessary omission notices for a small task. A complex app can still use fewer than six files. A narrowly requested schema or handoff need not acquire a brief, PRD, or companion package. Do not delete or rename useful existing files merely to reduce the count.

This is a coverage guide, not a required package:

| Topic | Include when relevant | Possible owner |
| --- | --- | --- |
| Product | Users, outcomes, scope, business rules, quality constraints | Brief or PRD |
| Flow | Entry, actors, prerequisites, transitions, failure and recovery | Brief or AFD |
| Design | Existing system, tokens/components, layout, states, content, accessibility | Brief, DBD, or supplied design system |
| Technical | Stack, boundaries, integration contracts, errors, operations | Brief or TRD |
| Data | Entities, relationships, ownership, integrity, lifecycle, access, migration | Brief or BSD |
| Delivery | Outcomes, dependencies, acceptance, tasks, verification, next step | Brief or IPD |

Add API contracts, security/privacy, operations/recovery, migrations, research, or architecture decisions only when they carry material information. An API-only project need not have screens; a local utility need not have a server. A full-package request still requires complete relevant coverage and navigation.

## Milestones and tasks

Keep the delivery plan in an existing owner, `docs/ipd.md`, or a delivery section of a small consolidated specification. Milestones and tasks are required coverage for implementation preparation, not a requirement for a particular filename or six-document package.

Define milestones as observable useful outcomes in dependency order. For each, record its scope, predecessor milestones, exit criteria, and tasks. Cover the whole bounded release, including setup, integration, verification, and distribution/operations only where needed. Put future releases outside this plan rather than inventing a detailed roadmap for them.

Each task needs a stable identifier, bounded result, linked requirements/contracts, dependencies, observable acceptance, a verification method, and readiness or blocker. Use the workspace's existing IDs and statuses. Otherwise use simple milestone/task IDs and distinguish Ready, Waiting on dependencies, and Blocked by an unresolved decision; keep execution progress and verification evidence separate. Never mark all tasks Ready just because their descriptions exist. A task relying on an unresolved material proposal is conditional or blocked, not unconditionally Ready.

Tasks should be small enough for a coherent implementation and review. Split vague items such as "build backend" when they hide distinct contracts or acceptance. Later tasks still need actionable results and checks, but not guessed filenames or unsupported commands. Give the next Ready task a self-contained handoff, inline or linked, using [the handoff guidance](#handoff-and-readiness). Do not require a separate task file for every row.

## Select specialized documents

These filenames are defaults only. Use the user's names or workspace conventions when established. The table identifies relevant content; apply the file-need decision above before creating a separate artifact. Do not automatically generate all six. If a requested document is inapplicable, explain why without inventing architecture or filler.

| Document | Useful coverage when needed | Default path and starting template |
| --- | --- | --- |
| PRD - Product Requirement Documentation | Multiple capabilities, roles, or business rules need a shared product contract beyond a short brief | `docs/prd.md`; [PRD template](../assets/templates/prd.md) |
| TRD - Technical Requirement Documentation | Architecture, quality constraints, integrations, or operational trade-offs need an explicit technical contract | `docs/trd.md`; [TRD template](../assets/templates/trd.md) |
| AFD - App Flow Documentation | Branching journeys, multiple roles, or state transitions need detailed success, rejection, and recovery flows | `docs/afd.md`; [AFD template](../assets/templates/afd.md) |
| DBD - Design Brief Documentation | User-facing screens need shared layout, component, responsive, or interaction decisions beyond existing design references | `docs/dbd.md`; [DBD template](../assets/templates/dbd.md) |
| BSD - Backend Schema Documentation | Backend persistence or backend data contracts need explicit relationships, ownership, access, or integrity rules | `docs/bsd.md`; [BSD template](../assets/templates/bsd.md) |
| IPD - Implementation Plan Documentation | Multiple implementation slices, dependencies, or handoffs need coordinated delivery and verification | `docs/ipd.md`; [IPD template](../assets/templates/ipd.md) |

Do not add a backend to justify BSD or UI to justify DBD. A frontend-only prototype may document local data in its brief or TRD. All six are appropriate only if each serves a distinct current need. Templates guide coverage, not mandatory sections; create honest drafts for unresolved topics rather than inventing decisions or waiting indefinitely to write.

## Optional starting points

- [Project brief](../assets/templates/project-brief.md): small project, consolidated context, or documentation index.
- [Feature specification](../assets/templates/feature-spec.md): behavior too complex for a paragraph.
- [Build handoff](../assets/templates/build-handoff.md): next bounded implementation task.

Translate headings, prose, and status labels according to the core language rule. Preserve IDs and technical identifiers. Replace placeholders and remove unused sections; record real unknowns with their impact. Specialized documents can use the coverage guide without another template library.

## Traceability without bureaucracy

Connect outcome → observable acceptance → work → verification/evidence. A few bullets may suffice; complex projects may need IDs and a table. Keep one canonical owner for each rule and status. Cover all requested features, expanding implementation detail only where dependencies are understood.

Acceptance describes starting conditions, action, and observable result, including material rejection or failure paths. Verification identifies method, data/environment, and expected result. Use commands only after checking the toolchain; otherwise state a logical procedure or label commands as proposed. Reading tests does not establish that they pass.

## Handoff and readiness

A handoff stands alone with linked inputs: result, exclusions, binding decisions, baseline, existing/proposed targets, dependencies, acceptance, verification, and blockers. Include a short copyable execution prompt when requested or handing work to another implementer. Task status stays in its owning plan.

Ready means the next task needs no guessing about material product behavior, permissions, or data contracts. It does not mean approved, implemented, tested, or released. Future decisions need not block independent work. If nothing is ready, identify the smallest unblocking action.

Perform one consistency pass at the requested scope. Check contradictions, links, coverage, and unsupported claims. After revisions, update affected dependents and mark obsolete evidence as historical. Close with actual outputs, coverage limits, and next action; do not add approval gates to authorized work.
