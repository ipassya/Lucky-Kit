# Planning from incomplete input

Use existing context to identify the user, their task, the first useful outcome, and hard constraints. For a vague idea, recommend a bounded first version and surface the uncertainty most likely to change it. Unless the user limits the request to exploration or another narrow outcome, carry that first version through specifications and a milestone/task plan in the same request. Explain choices through use, cost, and maintenance rather than a technology quiz. A draft permits labeled assumptions, not invented facts.

## Discover through focused questions

This probing interview is built into Lucky Kit; no separate interview skill is required. Its purpose is to uncover what the user wants and test how the plan holds together, not merely collect fields for documents.

Read relevant supplied material first. Identify what is known and the consequential decisions still open. When an answer is needed to determine material scope, permissions, money, ownership, or irreversible behavior, ask a focused question, normally one decision at a time. A small group of closely related questions is useful when the answers do not depend on each other. Do not make an interview a prerequisite for the whole plan, send a generic questionnaire, or ask for facts available in the workspace. Resolve routine reversible implementation choices with labeled assumptions rather than treating every unspecified detail as a blocker. If context is sufficient, produce the planning deliverables without requiring another prompt.

Choose the next question by its effect on scope, user behavior, design, feasibility, cost, or acceptance, not just whether work is blocked. Follow the answer into concrete consequences before switching topics. For example, if users share records, establish who can view, edit, delete, and recover them; if offline use matters, establish what happens to conflicting edits. Apply these examples only when relevant.

Replace vague preferences with scenarios: who encounters the problem, what they do now, what should happen on the main path, what failure looks like, and what can wait. Challenge contradictions and untested assumptions respectfully. Explain the practical trade-off, recommend a choice when useful, and let the user decide; do not disguise a recommendation as their requirement. Preserve settled choices unless new evidence exposes a material conflict.

For an uncertain user, offer concrete alternatives with consequences rather than demanding technical expertise. An unanswered question is not consent. Continue independent work with labeled reversible assumptions; keep decisions about money, access, ownership, and irreversible changes unresolved when intent is missing.

Ask necessary questions promptly and continue independent documentation while answers are pending. Once the application workspace and basic outcome are known, create or update a draft using [documents](documents.md). For implementation preparation, use a coherent proposed MVP and reversible design/technical assumptions to develop all relevant specifications, milestones, and tasks; do not stop at the initial brief or offer to create the rest later. For explicit exploration, keep the draft focused on the next decision. After meaningful answers, state what they change and reconcile affected specifications and tasks. Accept answers outside suggested options. Capture unresolved questions with their impact near the relevant rule and block only dependent work; do not treat proposals as approved or unresolved contracts as ready.

End discovery when the requested planning scope has clear outcomes, boundaries, material behavior, and observable acceptance, with remaining unknowns either deferred explicitly or attached to affected blocked work. For implementation preparation, finish the documentation and delivery plan as well; interview completion alone is not task completion. Do not pursue every imaginable edge case. If the user asks to stop questions or proceed with a draft, honor that and document uncertainty. An explicit discussion-only request remains in chat.

## Product and behavior

Describe the main journey, actors, prerequisites, success, rejection, and recovery. Resolve rules affecting ownership, money, access, or irreversible data changes before declaring dependent work ready. Defer later questions without blocking independent work. Record exclusions briefly; suggestions are not commitments.

## Technology and design

Start with the existing stack and design system. For a new system, recommend one coherent combination based on distribution, persistence, offline needs, integrations, team capability, budget, and operations. Explain the material trade-off and when an alternative would be better. Do not introduce services just to fill architecture categories.

Check official documentation for required compatibility, licensing, or pricing when it affects the decision. Separate documented support from a locally tested combination. If sources are unavailable, retain explicit uncertainty and propose a bounded experiment only when it blocks implementation.

Translate design direction into hierarchy, layout, semantic tokens, components, interaction states, accessibility, and realistic content for the main task. Reuse supplied tokens and components. A vague adjective such as "modern" is not a design rule. Keep requirements separate from proposed implementation details.

Use a sketch or preview when it resolves a real layout or interaction decision, or the user requests one. A text wireframe is a valid fallback. Label sample data and simulated actions. Distinguish creation, rendering, interaction checks, and user feedback. Feed accepted findings back into the owning specification.

## Delivery

Sequence work by dependencies and useful outcomes. A prototype or technical spike is conditional, not a mandatory first milestone. Existing projects can start with their next missing capability. For implementation preparation, cover the entire bounded first release with milestones and tasks using [documents](documents.md#milestones-and-tasks). Detail the next implementable task as a handoff and give every later in-scope task an actionable outcome, dependencies, acceptance, verification, and readiness without speculative file-by-file plans. Do not invent dates or capacity.

Use [documents](documents.md) when preparing durable specifications or a handoff. Stop at the requested result; planning does not itself initiate implementation.
