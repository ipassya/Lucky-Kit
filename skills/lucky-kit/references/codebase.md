# Document an existing codebase

Establish requested coverage and output location. "All workflow documents" means covering the relevant implemented system, not generating every possible template. Documentation does not authorize application code changes, dependency installation, migrations, or deployment.

## Inspect with a purpose

Start with repository instructions, documentation, manifests, directory structure, and entry points. Exclude generated output, dependency trees, secrets, and unrelated modules. Trace in-scope capabilities through relevant UI or caller, validation, authorization, domain logic, persistence, and external boundaries. Inspect schemas/migrations, configuration examples, jobs, and tests where they establish behavior or constraints.

Use targeted searches and maintain a compact coverage map of inspected modules, entry points, and gaps. Broaden beyond initial samples when covering the whole project. For large systems, work module by module with an index; do not claim comprehensive documentation while material areas remain uninspected.

Tests describe expected behavior; a test file is not execution evidence. An environment variable or dependency does not prove an integration is active. A hidden UI action does not prove backend authorization. A migration file does not prove deployment. Mark mocks, stubs, feature flags, and environment-dependent paths.

## Write from evidence

For important claims, retain a source path and symbol or line reference, plus revision/snapshot when available. Separate:

- Observed in source: behavior traceable to inspected implementation.
- Verified at runtime: actual check, environment, and result.
- Inferred or unknown: reasoning, missing context, and impact.
- Proposed: intended improvement, not current behavior.

Use descriptive equivalents in the output language. Never reconstruct business goals, approval, compliance, or production performance as facts. If asked for a PRD, label it a reconstructed current-state specification; distinguish inferred intent from supplied requirements.

Cover applicable product behavior, user/system flows, design conventions, architecture/integrations, data/access/lifecycle, and setup/operations. Describe gaps separately from plans. Use [documents](documents.md) to choose files; link good existing documentation instead of duplicating it. Do not invent a roadmap.

## Validate within scope

Cross-check names, routes, fields, roles, and relationships against their owning sources. Check links and consistency. Run relevant non-destructive checks only when authorized and useful; record unrun checks honestly. State coverage limits and unresolved code/document disagreements.

Without direct access, request a tree and relevant entry points, schemas, or excerpts incrementally. Produce a bounded partial draft from them. Never describe pasted samples as a full repository audit.
