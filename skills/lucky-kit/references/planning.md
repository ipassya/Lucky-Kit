# Planning from incomplete input

Use existing context to identify the user, their task, the first useful outcome, and hard constraints. For a vague idea, recommend a bounded first version and ask the question most likely to change it. Explain choices through use, cost, and maintenance rather than a technology quiz. A draft permits labeled assumptions, not invented facts.

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
