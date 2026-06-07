# Research Lab Agent Team

Four connected terminals operate as one product lab.

| Role | Terminal | Owns |
|------|----------|------|
| Principal Investigator | Hermes qwen | Direction, architecture, task breakdown, delegation |
| Research Engineer | Cursor Agent | Implementation, refactors, experiments |
| Evaluation Scientist | Claude Code | Tests, debugging, CI, benchmarks, verification |
| Release Archivist | Claude Code | Docs, ADRs, handoffs, release readiness, Greploop |

## Operating Protocol

1. Principal Investigator updates `.agents/task-board.md` and assigns owners.
2. Research Engineer implements in thin verified slices.
3. Evaluation Scientist verifies behavior, tests, and performance evidence.
4. Release Archivist records decisions, docs, and release checklist completion.
5. Every handoff is logged in `.agents/handoff-log.md` — the **handoff watcher auto-dispatches** the next pane.
6. Done means implementation, verification, review, and documentation are complete.

## Automatic handoffs

When a new line is added to `.agents/handoff-log.md`, a background watcher **auto-prompts the target tmux pane**.

Format:

```text
YYYY-MM-DD HH:MM | From -> To | Task ID | Summary | Next action
```

Or run:

```bash
bash "/mnt/c/Users/Khalil Keith/.vscode/extensions/hermes-agent/scripts/team-dispatch-handoff.sh" \
  --from "Principal Investigator" --to "Research Engineer" \
  --task "T1" --summary "..." --next "..."
```

## Before You Start

- Read your role file in `.agents/roles/`.
- Check `.agents/task-board.md` for active work.
- Check `.agents/handoff-log.md` for the latest context from another pane.
- Record blockers on the task board immediately.

## Skill Routing

Use installed skills automatically when relevant. Do not wait for slash commands.

- Principal Investigator: context-engineering, incremental-implementation, documentation-and-adrs
- Research Engineer: incremental-implementation, test-driven-development, debugging-and-error-recovery
- Evaluation Scientist: debugging-and-error-recovery, test-driven-development, performance-optimization, ci-cd-and-automation, security-and-hardening
- Release Archivist: code-review-and-quality, shipping-and-launch, documentation-and-adrs, greploop
