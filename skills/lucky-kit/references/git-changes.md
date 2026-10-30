# Finish documentation changes in Git

Use when the application workspace is already a Git repository and this task writes files. Discussion-only work has nothing to commit. Respect explicit no-commit or workspace restrictions: save authorized edits, leave them uncommitted, and do not stage them merely as a substitute for committing.

## Establish the baseline before editing

Inspect the repository root, HEAD, status, staged diff, and unstaged diff for affected files. Distinguish the task's work from existing user changes, including untracked files. Preserve existing content, staging intent, and unrelated changes. Do not initialize a repository, change Git identity/configuration, or clean the workspace to make this workflow convenient.

## Isolate the actual change

- When every change in the intended files belongs to this task, commit those files without accidentally including unrelated staged paths. Review the proposed commit diff, not only the working-tree diff.
- If a file contains both user changes and task changes, selecting its filename is insufficient: whole-file staging or a path-only commit can include unrelated hunks. Separate task hunks from the baseline using an appropriate selective or isolated-index approach only when their ownership and dependencies are clear. Preserve the user's existing staged and unstaged changes; do not reset, stash, discard, or temporarily rewrite their work just to simplify the commit.
- If changes overlap or cannot be isolated confidently, keep the useful edits and report that a safe task-only commit is blocked. Do not silently claim completion of the commit or bundle another person's work. Avoid leaving a partly modified index from an unsuccessful isolation attempt.

Commit a coherent update after applicable checks pass, not after every write. Do not create empty commits or amend an earlier commit just to hide another iteration. Before committing, verify the exact content intended for the commit and ensure the message describes that content.

## Failed checks or commit attempts

Inspect the failure. Fix an in-scope problem when the task authorizes the fix, rerun the affected check, then retry normally. An unrelated staged-file warning may be irrelevant to an isolated task-only commit; establish that the actual committed content passes its applicable checks rather than ignoring a failure in it.

If a hook rejects the commit, preserve the hook and its configuration. Do not use `--no-verify`, disable hooks, override their path, change their environment to skip checks, or rewrite policy files to force success. If the cause requires user action or a change outside scope, leave the task uncommitted and report the concrete failure and next action. Missing identity, signing, or access is also a blocker to report, not permission to change global configuration.

## Verify and report

Confirm the resulting commit exists and contains only the intended changes. Inspect remaining status/diffs so unrelated content and its staged/unstaged state stay intact. Report the hash and actual checks, or explicitly state no commit was made and why. A saved document, staged change, failed command, or clean working tree alone is not proof of a successful commit. Pushing is a separate action requiring the user's request.
