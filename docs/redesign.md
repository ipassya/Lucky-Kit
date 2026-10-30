# Lightweight redesign

## Decisions

The previous workflow defaulted to a Standard package with a README, six core documents, feature specifications, a handoff, and formal decision/assumption/question registers. That structure can help a large delivery but adds ceremony to small projects and users who already have good artifacts.

The redesign makes a short, vendor-neutral entrypoint sufficient for simple work. Four optional references cover planning, artifact alignment, codebase documentation, and document composition. Three compact templates replace fifteen specialized templates. A coverage guide retains product, flow, design, technical, data, and delivery concerns without requiring a separate file for each.

Removed: mandatory Standard/Extended profiles, default D/A/Q registers, obligatory ID chains, a separate visual exploration workflow, and duplicated status/verification instructions. Visual exploration and traceability remain conditional techniques. Existing project IDs and structure are preserved.

Added: explicit artifact conflict handling, source-based reconstruction of existing applications, plain-chat fallback, language routing, and an optional standard-library Python installer with an explicit host directory.

OpenAI UI metadata remains optional. Deleting it would reduce convenience for that host without improving the portability of the core. Multiple vendor adapters would add maintenance and drift without changing the shared instructions.

## Trade-offs

A smaller library provides fewer domain-specific prompts. Complex projects still need deliberate coverage and may require more detailed documents. The document guide supplies that coverage; user-requested comprehensive documentation takes precedence over brevity.

Plain text is widely transferable but does not make every model equally capable. Native progressive loading can reduce loaded context, while a chat that receives the entire library pays for all of it. The fallback therefore starts with the core alone.

An installer that retains unknown files protects local additions but cannot automatically remove obsolete content. Structural migrations use a clean replacement with a retained backup. This avoids a vendor-specific install manager and hidden deletion rules.

## Measurement and validation

Run `python scripts/measure-context.py --before /path/to/source-before` to compare normalized UTF-8 text. Core, optional references, and templates are measured separately. Characters and whitespace-delimited words are exact for that method. Characters divided by four is only a heuristic, especially across languages; actual input/output tokens, caching, and billed usage are not measured.

Package checks establish structure, links, and legal-file integrity. Installer tests cover filesystem behavior. Scenario walkthroughs can expose instruction gaps but do not establish independent or cross-model performance. Keep raw fixtures and evidence outside the repository; describe the method and limitations in the delivery report.
