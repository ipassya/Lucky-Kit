# Behavioral evaluation

Use realistic independent agent runs to check decisions that package validation cannot establish: document usefulness, depth appropriate to the user's purpose, focused discovery, and safe automatic commits. Run affected scenarios after workflow changes; ordinary spelling edits do not require the full evaluation.

The optional [evaluation helper](../scripts/evaluate-workflow.py) uses Python 3.10+ and Git. It has no model SDK or runtime role in the installed skill. Prompts, fixture repositories, transcripts, manifests, and reports are created outside the repository. Do not copy generated application output into Lucky Kit.

## Prepare an isolated run

Choose a new, nonexistent directory outside both this repository and the skill package:

```sh
python scripts/evaluate-workflow.py prepare --output /path/to/new-evaluation-run --skill /path/to/lucky-kit
```

Use the actual validated skill directory being evaluated. The command records its file hashes and the source repository revision/working-tree status. A revision alone does not identify uncommitted skill changes; retain the recorded fingerprint.

Each fixture receives its own local Git repository, baseline commit, repository-local synthetic identity, and no remote. The helper refuses existing output directories and destinations inside the repository or skill. A failed preparation is retained for diagnosis; use a different new destination for a retry.

The generated run contains:

- `prompts/`: task envelopes for agents, with realistic user requests and resource boundaries.
- `workspaces/`: four independent application workspaces.
- `manifest.json`: initial commits, index/worktree evidence, hook hashes, and package fingerprint.
- `review.md`: parent-only semantic rubric and space to record conclusions.

## Execute without teaching the expected answer

Use fresh agents without inherited discussion of the change or suspected failure. Give each agent only its generated prompt. Do not provide `review.md`, the expected output, suggested fixes, or a reminder to commit. Use the same model/settings for before-and-after comparisons when possible, and record actual changes to those settings.

The scenarios cover:

| Scenario | Requested outcome | Special condition |
| --- | --- | --- |
| `exploration-discovery` | Explore an early family-expenses idea | Judge consequential questions and exploratory depth; continue with a plausible answer to the actual first question |
| `decision-no-commit` | Recommend web versus native from supplied constraints | User explicitly prohibits committing |
| `handoff-mixed` | Update an existing support-ticket handoff | Separate staged and unstaged user edits already occupy the same file |
| `hook-failure` | Specify a backend schema | A deterministic pre-commit hook rejects commits |

After the first exploration question, relay a plausible answer and inspect whether the next question follows its consequences, the document updates, and proposals remain distinct from decisions. Record the actual answer; do not silently reuse a response that no longer fits a changed question. Respect any request to stop questioning in follow-up scenarios.

Do not equate a saved file with successful discovery or a large document set with complete coverage. Review who will use each artifact, what decision/work it supports, and whether its detail is appropriate for exploration, decision-making, or implementation handoff. A focused request can need a single document. Existing owners should be updated rather than duplicated.

## Evaluate idea-to-implementation planning

The helper's existing exploration scenario explicitly requests exploration. It does not establish that an ordinary idea prompt reaches implementation preparation. Exercise the following requests in separate external workspaces when changing that default; the helper does not generate these additional fixtures:

| Request | Review focus |
| --- | --- |
| One idea prompt for a small local app with known scope and stack, without naming document types | The output includes relevant specifications and milestones/tasks for the whole first release, plus the next task's handoff, without a follow-up request. A consolidated specification is acceptable; unnecessary backend or six-file scaffolding is not. |
| One idea prompt for a multi-user app with a material access or ownership decision unresolved | Independent specifications and a full scoped delivery plan still appear. The missing decision is asked, affected tasks are blocked, and neither proposals nor the entire package are falsely declared Ready. Substantial contracts may justify separate documents. |
| An explicit exploration-only or chat-only request | The agent respects requested depth and destination; exploration does not acquire an unrequested implementation package, and chat-only produces no saved application documents. |
| A targeted update to an existing schema or task | The established owner and necessary dependents change without a new brief or unrelated full-release backlog. |

Inspect actual task outcomes, source links, dependencies, acceptance, verification, readiness, milestone exit criteria, and coverage of all in-scope capabilities. "Build the app" or a detailed first task followed by vague future headings is insufficient. Check that no application implementation was initiated by planning alone. Record whether the exercise was a self-review walkthrough or an independent agent execution; a walkthrough is not evidence of runtime agent behavior.

## Inspect actual results

```sh
python scripts/evaluate-workflow.py inspect --run-dir /path/to/evaluation-run
```

Inspection prints JSON facts to stdout. Redirect it to a results file outside the application workspaces if desired. It reads Git state with optional index refresh disabled; it does not stage, commit, reset, clean, or rewrite files. It reports commits, committed paths and diffs, current staged/unstaged diffs, file hashes, local Git configuration, and hook integrity. It also reports whether the evaluated skill changed since preparation. Treat inspection errors as failures to collect evidence, not passing scenarios.

For mixed work, compare the manifest's original head/index/worktree text with the result's three versions. Task-only commit success must preserve unrelated user edits and their staged versus unstaged distinction. A safe refusal with a clear blocker may satisfy preservation, but it is **not** proof that automatic commit succeeded in that case. A whole-file commit that bundles user changes fails even if the working tree is clean.

For hook failure, check that no commit was created, the hook and its configuration were preserved, task output remains available, and the final reply explains the failure. Do not bypass the hook to make the test green. For the no-commit case, saved output is expected but a new commit violates the request.

The helper does not score semantic behavior, exact headings, file counts, or word counts. Those are evidence for human review, not a substitute for judging the user's outcome. It does not trace every subprocess the agent ran; preserved final hook state alone cannot prove that no temporary bypass was attempted. Review available execution records when that distinction matters.

## Compare and retain evidence

Keep separate run directories for the baseline and candidate. Compare their inspection JSON and semantic reviews by scenario: which artifacts changed, whether accepted decisions were preserved, whether questions improved, what was committed, and what remained blocked. Record the prompt, source fingerprint, agent/model or review method, environment, expected behavior, observed outcome, and material limitations.

Never replace a failure with an unlabeled retry or describe self-review as an independent agent test. Fix only demonstrated problems, rerun affected scenarios, and retain both outcomes. These local synthetic cases do not establish implicit skill selection by every host, cross-model reliability, remote Git permissions, hosted CI success, or application readiness.

## Test the helper itself

```sh
python scripts/test-evaluate-workflow.py
```

These tests verify isolated fixture setup, refusal of unsafe/existing destinations, read-only inspection, real hook rejection, and separate committed/index/worktree evidence. They do not run a model or prove the skill chooses well. The fixtures and test outputs remain in temporary directories outside the repository.
