# Choose and connect documents

Honor requested formats and existing paths. Otherwise use Markdown and start with one brief. Split topics when size, audience, ownership, or independent updates justify it. Do not overwrite an operational README with planning boilerplate.

This is a coverage guide, not a required package:

| Topic | Include when relevant | Possible owner |
| --- | --- | --- |
| Product | Users, outcomes, scope, business rules, quality constraints | Brief or PRD |
| Flow | Entry, actors, prerequisites, transitions, failure and recovery | Brief or app-flow document |
| Design | Existing system, tokens/components, layout, states, content, accessibility | Design brief or supplied design system |
| Technical | Stack, boundaries, integration contracts, errors, operations | Technical specification |
| Data | Entities, relationships, ownership, integrity, lifecycle, access, migration | Data model or schema document |
| Delivery | Outcomes, dependencies, acceptance, tasks, verification, next step | Brief or implementation plan |

Add API contracts, security/privacy, operations/recovery, migrations, research, or architecture decisions only when they carry material information. An API-only project need not have screens; a local utility need not have a server. A full-package request still requires complete relevant coverage and navigation.

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
