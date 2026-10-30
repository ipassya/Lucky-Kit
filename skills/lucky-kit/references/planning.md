# Planning from incomplete input

Use existing context to identify the user, their task, the first useful outcome, and hard constraints. For a vague idea, recommend a bounded first version and ask the question most likely to change it. Explain choices through use, cost, and maintenance rather than a technology quiz. A draft permits labeled assumptions, not invented facts.

## Discover through focused questions

This probing interview is built into Lucky Kit; no separate interview skill is required. Its purpose is to uncover what the user wants and test how the plan holds together, not merely collect fields for documents.

Read relevant supplied material first. Identify what is known and the consequential decisions still open, then explore one decision at a time by default. A small group of closely related questions is useful when the answers do not depend on each other. Do not send a generic questionnaire or ask the user for facts available in the workspace.

Choose the next question by its effect on scope, user behavior, design, feasibility, cost, or acceptance, not just whether work is blocked. Follow the answer into concrete consequences before switching topics. For example, if users share records, establish who can view, edit, delete, and recover them; if offline use matters, establish what happens to conflicting edits. Apply these examples only when relevant.

Replace vague preferences with scenarios: who encounters the problem, what they do now, what should happen on the main path, what failure looks like, and what can wait. Challenge contradictions and untested assumptions respectfully. Explain the practical trade-off, recommend a choice when useful, and let the user decide; do not disguise a recommendation as their requirement. Preserve settled choices unless new evidence exposes a material conflict.

For an uncertain user, offer concrete alternatives with consequences rather than demanding technical expertise. An unanswered question is not consent. Continue independent work with labeled reversible assumptions; keep decisions about money, access, ownership, and irreversible changes unresolved when intent is missing.

Ask the priority question promptly. Once the application workspace and basic outcome are known, create or update a draft using [documents](documents.md), even while discovery continues. During exploration, keep that draft focused on what helps the next decision rather than elaborating architecture and tasks before basic intent is understood. After meaningful answers, state what they change, probe the next consequential uncertainty, and reconcile the affected sections and dependents. Accept answers outside suggested options. Capture unresolved questions with their impact near the relevant rule; do not treat drafts as approved or ready.

End discovery when the requested planning scope has clear outcomes, boundaries, material behavior, and observable acceptance, with remaining unknowns either deferred explicitly or attached to affected blocked work. Do not pursue every imaginable edge case. If the user asks to stop questions or proceed with a draft, honor that and document uncertainty. An explicit discussion-only request remains in chat.

## Product and behavior

Describe the main journey, actors, prerequisites, success, rejection, and recovery. Resolve rules affecting ownership, money, access, or irreversible data changes before declaring dependent work ready. Defer later questions without blocking independent work. Record exclusions briefly; suggestions are not commitments.

## Technology and design

Start with the existing stack and design system. For a new system, recommend one coherent combination based on distribution, persistence, offline needs, integrations, team capability, budget, and operations. Explain the material trade-off and when an alternative would be better. Do not introduce services just to fill architecture categories.

Check official documentation for required compatibility, licensing, or pricing when it affects the decision. Separate documented support from a locally tested combination. If sources are unavailable, retain explicit uncertainty and propose a bounded experiment only when it blocks implementation.

Translate design direction into hierarchy, layout, semantic tokens, components, interaction states, accessibility, and realistic content for the main task. Reuse supplied tokens and components. A vague adjective such as "modern" is not a design rule. Keep requirements separate from proposed implementation details.

Use a sketch or preview when it resolves a real layout or interaction decision, or the user requests one. A text wireframe is a valid fallback. Label sample data and simulated actions. Distinguish creation, rendering, interaction checks, and user feedback. Feed accepted findings back into the owning specification.

## Delivery

Sequence work by dependencies and useful outcomes. A prototype or technical spike is conditional, not a mandatory first milestone. Existing projects can start with their next missing capability. Detail the next implementable slice; give later work scope, dependencies, and acceptance without speculative file-by-file plans. Do not invent dates or capacity.

Use [documents](documents.md) when preparing durable specifications or a handoff. Stop at the requested result; planning does not itself initiate implementation.
