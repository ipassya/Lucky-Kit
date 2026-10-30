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

## Delivery and prototypes

Use the sequence below as an adaptable delivery plan, not mandatory phases, document names, or approval gates. Reuse evidence already available; merge or skip work with a concrete reason. Existing projects start at the next useful gap. Document the whole bounded release now while keeping later details conditional on findings that could change them.

| Work | Intended result and evidence needed to continue |
| --- | --- |
| Understand the problem | Actors, current scenario, desired outcome, constraints, and consequential unknowns. Distinguish user evidence from hypotheses; reuse known answers. |
| Bound the release and draft specifications | In-scope capabilities, important flows, acceptance, proposed design/data/technical boundaries, and a delivery plan. Do not wait for every detail or freeze untested choices. |
| Test consequential assumptions where needed | A targeted prototype for interaction uncertainty, or a bounded technical experiment for feasibility. State the question and choose the least costly fidelity that can answer it. |
| Evaluate and reconcile | Record actual observations, unresolved findings, and whether to proceed, revise, or defer. Update the owning specifications, contracts, acceptance, dependencies, and affected task readiness. |
| Implement useful functional slices | Each slice completes a bounded user outcome across applicable UI, rules, data, and interfaces, with its own verification. Keep enabling setup small; avoid building every layer before the first real flow works. |
| Verify the whole outcome and hand off | Check cross-slice behavior, access, failures, accessibility, and relevant quality constraints. Include distribution, operations, and release checks only within scope; separate planning, implementation, test evidence, and release readiness. |

For a new user-facing app with untested consequential interactions, normally plan a targeted prototype and evaluation before committing dependent implementation details. Honor an explicit prototype-first request. Skip a separate prototype when existing evidence already answers the question, the change is straightforward, or the product has no relevant UI uncertainty. An API-only app may need a technical experiment instead, and neither technique is required without an actual uncertainty. Do not introduce screens or a backend to justify an experiment.

"Prototype first" changes sequencing; it does not mean "prototype only". Unless the user explicitly limits scope, retain specifications, milestones, and actionable tasks for the whole bounded release, with prototype work detailed first and dependent implementation labeled conditional where necessary. If the user asks only for a prototype, limit documentation and delivery to its purpose and evaluation; do not add a full MVP backlog. Planning either path does not itself authorize building the prototype or application.

### Define the prototype or experiment

Record its question or hypothesis, target actor/scenario, chosen fidelity and rationale, included paths and important failure states, sample data, working versus simulated actions, exclusions, evaluation method, observable success criteria, and follow-up decision. A sketch can test layout; an interactive mock can test navigation; a functional slice or technical experiment is needed to test persistence or integration behavior. Do not present simulated login, access, payments, or storage as proof that the real contract works. Use synthetic data where real data is unnecessary.

Give creation and evaluation distinct task outcomes, even if one small milestone contains both. Building, rendering, clicking through, heuristic review, and feedback from actual users are different evidence. Name the method and environment and report only observations actually obtained. A self-check must not be called user validation. If feedback is unavailable, mark evaluation pending and only the dependent decisions/tasks conditional; still complete the independent planning work.

Reconcile findings before implementing behavior they could invalidate. State whether prototype code will be discarded, selectively reused after checking its suitability, or evolved as an intentionally functional slice; polished mock code is not automatically a production foundation. Do not require approval for every stage or stop authorized independent work while waiting for unrelated feedback.

For implementation preparation, cover the entire bounded first release with milestones and tasks using [documents](documents.md#milestones-and-tasks). Detail the next implementable task as a handoff and give every later in-scope task an actionable outcome, dependencies, acceptance, verification, and readiness without speculative file-by-file plans. Verification belongs in each slice as well as final cross-slice checks. Do not invent dates, capacity, or test/user-feedback results.

Use [documents](documents.md) when preparing durable specifications or a handoff. Stop at the requested result; planning does not itself initiate implementation.
