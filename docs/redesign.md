# Lightweight redesign

## Decisions

The previous workflow defaulted to a Standard package with a README, six core documents, feature specifications, a handoff, and formal decision/assumption/question registers. That structure can help a large delivery but adds ceremony to small projects and users who already have good artifacts.

The redesign makes a short, vendor-neutral entrypoint sufficient for simple work. Four optional references cover planning, artifact alignment, codebase documentation, and document composition. The initial redesign replaced fifteen specialized templates with three compact starting points. The current package also provides six conditional PRD, TRD, AFD, DBD, BSD, and IPD templates. A coverage guide retains product, flow, design, technical, data, and delivery concerns without requiring a separate file for each.

Removed: mandatory Standard/Extended profiles, default D/A/Q registers, obligatory ID chains, a separate visual exploration workflow, and duplicated status/verification instructions. Visual exploration and traceability remain conditional techniques. Existing project IDs and structure are preserved.

Added: explicit artifact conflict handling, source-based reconstruction of existing applications, plain-chat fallback, language routing, and an optional standard-library Python installer with an explicit host directory.

The initial chat-only-unless-saving-was-requested rule also suppressed expected planning artifacts. App planning now authorizes saved drafts in the application's workspace, with an explicit chat-only/review-only exception and a clear fallback when file access is unavailable. Discovery probes consequential decisions rather than only immediate blockers. Documents are updated during discovery so an unfinished interview does not prevent useful drafts. Specialized documents are created when their selection criteria apply, not merely suggested or generated as a mandatory package.

File selection now explicitly considers the reader, the decision or work served, and whether an existing owner can carry the content. Topic coverage is not a trigger to create a file: even complex applications may need fewer than six documents, and focused requests need no companion package. Separate files are justified by the current request, meaningful detail, ownership, or maintenance needs rather than template availability.

Creation and revision share a proportional quality loop: inspect context, change the owning content, reconcile dependents, review the result, and run relevant checks. Validated task updates are committed automatically in an existing Git repository, preserving unrelated work and honoring user/workspace exceptions. The workflow does not initialize repositories, push, or bypass failed checks. A missing repository or unsafe mixed changes is reported, not silently worked around.

Depth is now inferred from the next use: exploration, decision support, or implementation handoff. These are not mandatory phases or document sets. Early discovery asks consequential questions promptly and avoids detailed architecture before basic intent is understood. Existing documents deepen as needed. The built-in probing interview remains active, including follow-up reasoning, accepting answers outside suggested options, and respecting a request to stop questions.

Mixed Git changes are assessed against HEAD, index, and working tree, including changes within one file. Hook failures and no-commit requests have explicit boundaries. Repeatable evaluation tooling prepares fixtures outside the repository and inspects observable facts separately from human judgments of relevance, depth, and discovery. A safe blocked commit is reported separately from successful automatic committing.

OpenAI UI metadata remains optional. Deleting it would reduce convenience for that host without improving the portability of the core. Multiple vendor adapters would add maintenance and drift without changing the shared instructions.

## Trade-offs

A compact library provides fewer domain-specific prompts. Complex projects still need deliberate coverage; conditional specialized templates support that without loading them for every task. User-requested comprehensive documentation takes precedence over brevity. Focused discovery can require multiple turns; stop when the requested scope is sufficiently clear or the user asks to proceed with explicit unknowns.

Plain text is widely transferable but does not make every model equally capable. Native progressive loading can reduce loaded context, while a chat that receives the entire library pays for all of it. The fallback therefore starts with the core alone.

An installer that retains unknown files protects local additions but cannot automatically remove obsolete content. Structural migrations use a clean replacement with a retained backup. This avoids a vendor-specific install manager and hidden deletion rules.

## Measurement and validation

Run `python scripts/measure-context.py --before /path/to/source-before` to compare normalized UTF-8 text. Core, optional references, and templates are measured separately. Characters and whitespace-delimited words are exact for that method. Characters divided by four is only a heuristic, especially across languages; actual input/output tokens, caching, and billed usage are not measured.

Package checks establish structure, links, and legal-file integrity. Installer tests cover filesystem behavior. Scenario walkthroughs can expose instruction gaps but do not establish independent or cross-model performance. Keep raw fixtures and evidence outside the repository; describe the method and limitations in the delivery report.
