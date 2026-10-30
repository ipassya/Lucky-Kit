# Lightweight redesign

## Decisions

The previous workflow defaulted to a Standard package with a README, six core documents, feature specifications, a handoff, and formal decision/assumption/question registers. That structure can help a large delivery but adds ceremony to small projects and users who already have good artifacts.

The redesign makes a short, vendor-neutral entrypoint sufficient for simple work. Four optional references cover planning, artifact alignment, codebase documentation, and document composition. The initial redesign replaced fifteen specialized templates with three compact starting points. The current package also provides six conditional PRD, TRD, AFD, DBD, BSD, and IPD templates. A coverage guide retains product, flow, design, technical, data, and delivery concerns without requiring a separate file for each.

Removed: mandatory Standard/Extended profiles, default D/A/Q registers, obligatory ID chains, a separate visual exploration workflow, and duplicated status/verification instructions. Visual exploration and traceability remain conditional techniques. Existing project IDs and structure are preserved.

Added: explicit artifact conflict handling, source-based reconstruction of existing applications, plain-chat fallback, language routing, and an optional standard-library Python installer with an explicit host directory.

The initial chat-only-unless-saving-was-requested rule also suppressed expected planning artifacts. App planning now authorizes saved drafts in the application's workspace, with an explicit chat-only/review-only exception and a clear fallback when file access is unavailable. Discovery probes consequential decisions rather than only immediate blockers. Documents are updated during discovery so an unfinished interview does not prevent useful drafts. Specialized documents are created when their selection criteria apply, not merely suggested or generated as a mandatory package.

File selection now explicitly considers the reader, the decision or work served, and whether an existing owner can carry the content. Topic coverage is not a trigger to create a file: even complex applications may need fewer than six documents, and focused requests need no companion package. Separate files are justified by the current request, meaningful detail, ownership, or maintenance needs rather than template availability.

Creation and revision share a proportional quality loop: inspect context, change the owning content, reconcile dependents, review the result, and run relevant checks. Validated task updates are committed automatically in an existing Git repository, preserving unrelated work and honoring user/workspace exceptions. The workflow does not initialize repositories, push, or bypass failed checks. A missing repository or unsafe mixed changes is reported, not silently worked around.

Depth follows the requested outcome, with implementation preparation as the default for a new app idea. Previously, the exploratory interpretation and repeated preference for consolidation could let an agent stop at a brief and omit delivery work. A single idea prompt now carries through relevant specifications, milestones, and tasks across a bounded first release. A brief remains a valid initial draft or a small complete specification; it does not define completion. Explicit exploration, decision support, review, and targeted-document requests retain their narrower scope.

Focused discovery supports that outcome rather than requiring an interview before all planning work. Known answers and reversible assumptions support independent specifications and tasks; unresolved material decisions block dependent work and prevent an unconditional readiness claim. Milestones have outcomes and exit criteria, every in-scope task has actionable acceptance and verification, and the next Ready task has a handoff. Splitting substantial topics is encouraged when it improves usability, without restoring a mandatory six-document package.

Delivery now has an explicit adaptable sequence in [the planning reference](../skills/lucky-kit/references/planning.md#delivery-and-prototypes): understand the problem, bound the release and draft specifications, test consequential assumptions where warranted, evaluate and reconcile, implement useful functional slices, then verify and hand off within scope. Prototype-first requests change the order without dropping the full-release plan; prototype-only requests remain bounded. Experiments have learning objectives and observable evaluation criteria, and their findings update specifications and task dependencies. Functional verification belongs within each slice as well as final integration checks.

This is Lucky Kit's synthesis of problem-led [discovery](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works), targeted experiments during [alpha](https://www.gov.uk/service-manual/agile-delivery/how-the-alpha-phase-works), iterative delivery during [beta](https://www.gov.uk/service-manual/agile-delivery/how-the-beta-phase-works), and [Agile principles](https://agilemanifesto.org/principles.html). It does not import government phase durations, assessments, public release obligations, or a fixed approval chain. A prototype may be skipped when evidence already resolves the relevant uncertainty; rendering, self-checks, actual user feedback, and functional verification remain different evidence.

Mixed Git changes are assessed against HEAD, index, and working tree, including changes within one file. Hook failures and no-commit requests have explicit boundaries. Repeatable evaluation tooling prepares fixtures outside the repository and inspects observable facts separately from human judgments of relevance, depth, and discovery. A safe blocked commit is reported separately from successful automatic committing.

OpenAI UI metadata remains optional. Deleting it would reduce convenience for that host without improving the portability of the core. Multiple vendor adapters would add maintenance and drift without changing the shared instructions.

## Trade-offs

A compact library provides fewer domain-specific prompts. Complex projects still need deliberate coverage; conditional specialized templates support that without loading them for every task. Implementation preparation requires more detail than an exploratory brief, but not a fixed file count. One prompt can produce a complete planning draft; missing material decisions can still require follow-up before dependent tasks become Ready. Do not invent user intent to promise a fully implementation-ready result from insufficient input.

Plain text is widely transferable but does not make every model equally capable. Native progressive loading can reduce loaded context, while a chat that receives the entire library pays for all of it. The fallback therefore starts with the core alone.

An installer that retains unknown files protects local additions but cannot automatically remove obsolete content. Structural migrations use a clean replacement with a retained backup. This avoids a vendor-specific install manager and hidden deletion rules.

## Measurement and validation

Run `python scripts/measure-context.py --before /path/to/source-before` to compare normalized UTF-8 text. Core, optional references, and templates are measured separately. Characters and whitespace-delimited words are exact for that method. Characters divided by four is only a heuristic, especially across languages; actual input/output tokens, caching, and billed usage are not measured.

Package checks establish structure, links, and legal-file integrity. Installer tests cover filesystem behavior. Scenario walkthroughs can expose instruction gaps but do not establish independent or cross-model performance. Keep raw fixtures and evidence outside the repository; describe the method and limitations in the delivery report.
