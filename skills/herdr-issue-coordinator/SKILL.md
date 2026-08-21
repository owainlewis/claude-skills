---
name: herdr-issue-coordinator
description: "Coordinates a batch of GitHub issues through separate Claude Code sessions running in visible Herdr tabs, with tested pull requests, review loops, and gated merges. Use when the user asks one Claude session to sequence several coding sessions, or to complete a parent issue, milestone, or issue batch inside Herdr."
user-invocable: true
argument-hint: "<parent issue, milestone, or issue list>"
---

# Herdr issue coordination

Use this session as the coordinator. Give each dispatched GitHub issue its own
git worktree, branch, Herdr tab, and Claude Code session. Sequence the work.
Keep implementation context in workers and all durable state in GitHub.

This skill is experimental. It depends on the `herdr` CLI and its API changes
between versions. Verify the commands below against the installed binary before
relying on them.

Explicitly naming `/herdr-issue-coordinator`, or explicitly telling the
coordinator that agents may merge, authorizes in-scope workers to merge their
own pull requests after every merge gate below passes. An implicit skill match
does not grant merge authority: run in no-merge mode unless the user's words
grant it. Neither mode authorizes deployment, release publication, destructive
operations, branch-protection bypasses, or changes outside the supplied batch.

## Preconditions

Stop if any of these fail. Do not substitute hidden subagents for workers.

1. `test "${HERDR_ENV:-}" = 1`. You must be running inside a Herdr pane.
2. `herdr --version` reports 0.8.0 or later. Earlier versions have no
   `agent prompt` and no `agent start --pane`, and this skill will not work.
3. `herdr agent` lists `prompt`, and `agent start` accepts `--kind` and
   `--pane`. The binary is the authority, not this document.
4. The working directory is a git repository with a GitHub remote and `gh`
   authenticated.
5. Read the repository instructions, parent issue, sub-issues, declared
   dependencies, project board, issue state, and linked open or merged pull
   requests. A merged pull request is only evidence of completion when it
   closes or explicitly references the issue and its final change and proof
   satisfy the issue scope. Reconcile that state instead of dispatching again.
6. Make every issue a complete task before dispatch. If a missing product or
   technical decision could change behavior, data, security, compatibility,
   operations, cost, or proof, mark that issue as needing human input.
7. Build a dependency graph. Stop for human correction on a dependency cycle.

## State rules

The coordinator is the only writer of batch state. These rules exist because a
sequenced batch runs for hours and this session's context is not durable.

- GitHub holds issue, pull request, review, and merge state. Re-read it at the
  start of every cycle. Never cache it across cycles.
- Never create a second tracker: no local state file, no notes file, no
  in-context list treated as authoritative.
- Workers never write batch state. They own one issue and report back.
- Workers never write their own tab status. The coordinator pushes it.
- If your own context is compacted mid-batch, re-derive the whole graph from
  GitHub before dispatching anything.

## Concurrency and tabs

- Default to 1 active worker. Use 2 only when two issues are independent and
  the user asked for speed. Use another limit only when the user asks.
- One tab per active issue. Close it after its merge is verified.
- Never leave finished tabs open. A long batch must not accumulate tabs.
- Keep the user's focus in the coordinator tab.

## Coordinator workflow

1. Name this tab for the batch.

   ```bash
   herdr tab rename "$HERDR_TAB_ID" "Coordinator"
   ```

   `tab rename` has no `--clear`. Record the original label and restore it
   verbatim when the batch ends.

2. Dispatch only issues whose prerequisites are merged. For each one, create
   the worktree first, then the tab, then the agent.

   ```bash
   # 1. worktree, from the updated remote default branch
   git worktree add -b <branch> <worktree-path> origin/<default-branch>

   # 2. tab, in this workspace, rooted in the worktree
   herdr tab create --workspace "$HERDR_WORKSPACE_ID" \
     --cwd <worktree-path> --label "#<issue> <short title>" --no-focus
   # read .result.tab.tab_id and .result.root_pane.pane_id from the response

   # 3. agent, in that tab's root pane
   herdr agent start issue-<issue> --kind claude --pane <root-pane-id>

   # 4. reclaim focus; agent start has no --no-focus and takes it
   herdr tab focus "$HERDR_TAB_ID"
   ```

   Agent names must match `[a-z][a-z0-9_-]{0,31}` and be unique among live
   agents, so `#123` is not a legal name. Use `issue-123` as the agent name and
   `#123 <short title>` as the tab label. Parse every id from the JSON
   response. Do not predict ids.

   If the issue already has an open pull request, use that pull request's exact
   head branch instead of creating a new one, and pass the branch and pull
   request URL in the worker prompt.

3. `agent start` returns only once Herdr sees the agent ready. It reports
   `agent_status` and `interactive_ready`. Do not add a separate wait.

4. Send the worker its task and wait for it to settle.

   ```bash
   herdr agent prompt issue-<issue> "<worker prompt>" --wait --timeout <ms>
   ```

   `agent prompt` submits text and Enter atomically. `--wait` returns on the
   first settled `idle`, `done`, or `blocked` state. Do not use `agent send`
   followed by a separate Enter.

5. Read a worker only when it needs help or reports completion.

   ```bash
   herdr agent get  issue-<issue>
   herdr agent read issue-<issue> --source recent-unwrapped --lines 200
   ```

   `agent read` returns plain text, not JSON. If a completed response is longer
   than the pane can return, ask the worker to write its full response to a
   temporary file and reply with only the path, then read that file.

6. On `blocked`, inspect before answering. Send a decision or corrected scope
   with `agent prompt`. Never edit a worker's files from the coordinator.

7. Push the current stage into the worker's tab after every state change.

   ```bash
   herdr pane report-metadata <pane-id> --source coordinator \
     --title "#<issue> <stage>" --ttl-ms 900000
   ```

   Stages are pipeline stages a human can act on, such as `implementing`,
   `tests running`, `PR open`, `awaiting CI`, `in review`, `blocked: <reason>`.
   Derive each one from GitHub, not from what the worker claimed. Refresh it
   every cycle so the TTL never lapses on a live worker.

8. After three failed attempts at the same check or review finding, stop that
   issue, record the evidence on the GitHub issue, and request human input.
   Continue other independent work.

9. When a worker reports completion, verify on GitHub before touching the tab.
   In merge mode: confirm the pull request is merged, the issue holds final
   proof, and the issue is closed. Close it explicitly if the merge did not.
   Mark it Done when the project supports it. Only then clean up:

   ```bash
   herdr tab close <tab-id>
   git worktree remove <worktree-path>
   ```

   Verify first, then close. Closing kills the worker process and its pane
   transcript. Never close a tab to end a problem you have not resolved.

   In no-merge mode: stop the worker once its pull request passes every
   agent-completable gate, leave the issue in Review, record the pending human
   merge as its blocker, and leave the tab open for the user.

10. Refresh the dependency graph from GitHub after every merge and dispatch the
    next ready issue from the updated default branch. Never start dependent
    work from an unmerged branch. In no-merge mode, record a blocked dependent
    as waiting on a human merge rather than waiting indefinitely.

11. Finish when every in-scope issue is merged and closed, or has a recorded
    blocker needing human action. In no-merge mode, finish when every in-scope
    issue has a ready pull request or a recorded blocker. Restore the
    coordinator tab label and confirm no worker tabs or worktrees remain.

## Worker contract

Each worker owns one issue and follows this order:

1. Read the issue, repository instructions, relevant design, code, tests, and
   dependency pull requests. Move the issue to In Progress when possible.
2. Work in the worktree it was started in. Do not create another worktree, do
   not change branch, and do not touch another issue's files.
3. Implement only the issue. Add or update tests for every acceptance
   criterion, affected failure path, regression risk, and named edge case.
4. Prove the change. Browser-facing work requires a real browser check of the
   affected success and failure flows, responsive widths, keyboard behavior,
   console errors, and failed requests when relevant.
5. Commit and push. Open a draft pull request if one is not already open, with
   a short summary and current proof.
6. Mark the pull request ready for review and move the issue to Review before
   requesting independent review.
7. Run an independent review with a fresh subagent that did not write the
   change. Wait for required CI and automated review. In merge mode, also wait
   for every repository-required approval. In no-merge mode, record a pending
   required approval as a human blocker rather than waiting indefinitely.
8. Address every valid in-scope finding. Reply to review threads with the fix
   or the evidence for making no change. Resolve a thread only when it is fully
   addressed.
9. After any code change, repeat the affected proof and a fresh review, push,
   update the pull request evidence, and wait for CI again. Iterate until the
   mode's gates pass. Do not manufacture extra rounds.
10. In merge mode, merge after every gate passes, using the repository's
    preferred method and never an admin bypass. Wait until GitHub reports the
    merge, record final proof, and verify the issue is closed. In no-merge
    mode, leave the passing pull request open. Report the final state.

## Merge gates

A worker may merge only when all of these are true:

- The pull request is ready for review, not draft.
- The complete issue scope and acceptance criteria have recorded proof.
- Focused and required wider tests pass on the final commit.
- An independent review verdict is `Approve` on the final code.
- Every required GitHub check passes.
- Every actionable automated or human review thread is resolved.
- Every repository-required approval is present.
- The pull request is mergeable and current with its required base.
- No security, data-loss, compatibility, operational, or product decision is
  unresolved.
- The pull request changes only the worker's issue.

If a gate cannot pass, do not merge. Record the blocker and continue other
independent work.

## Worker prompt

Use this shape and replace every placeholder:

```text
Complete <issue URL> in this worktree. It is already checked out on the
branch you should use.

You own only this issue, worktree, branch, and pull request.
Branch state: <reuse PR head branch and PR URL, or the new branch name>.
Delivery mode: <merge after all gates pass, or leave the passing PR open>.
Read the issue and repository instructions as the source of truth.
Implement the smallest complete change and prove acceptance criteria, edge
cases, failure paths, and regressions.

After local proof passes, commit, push, open or update the pull request, and
mark it ready for review. Only then run an independent review with a fresh
subagent and wait for CI and GitHub review. Address valid findings and repeat
proof and review after every code change.

Do not report your own status anywhere outside this session. The coordinator
tracks state from GitHub.

<If merge mode: The user explicitly authorized this run to merge this issue's
pull request after every merge gate passes. Wait until GitHub reports the
merge, update and close the issue, and return the result.>
<If no-merge mode: Leave the passing pull request open for human merge and
return its URL and proof.>
Do not deploy, publish a release, bypass repository rules, or change unrelated
work.
```

## Boundaries

- Use visible Herdr tabs for workers. Fresh subagents are only for the
  independent review inside a worker.
- Never dispatch two workers for one issue, or let two workers share a worktree.
- Never replace or duplicate an existing pull request for the issue. Resume it.
- Never start dependent work from an unmerged pull request.
- Never merge an unrelated pull request merely because it blocks the batch.
- Never infer deployment or release authority from merge authority.
- Never close a tab, pane, workspace, or worktree you did not create.
- Never run `herdr server stop`. It would kill this session.

## Known Herdr behavior

Verified against herdr 0.8.0, protocol 19.

- `agent start` has no `--no-focus` and takes focus. Follow it with
  `herdr tab focus "$HERDR_TAB_ID"`.
- `tab rename` has no `--clear`, unlike `agent rename`. Restore labels by hand.
- `agent read` returns plain text. Other commands return JSON.
- `herdr worktree create` creates a whole workspace per worktree, and
  `herdr worktree remove` is workspace-scoped. It does not fit one tab per
  issue in a single workspace. Use `git worktree add` instead.
- `pane report-metadata --title` is stored on the pane, not on the tab, and
  `tab list` does not return it.
