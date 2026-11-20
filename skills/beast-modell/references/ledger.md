# Beast-ModeLL ledger

The ledger is the memory. It lives in the project or workspace the agent works in, not in this repo, so each project keeps its own memory and nothing crosses over.

## Location

Use the first that applies:

1. A `.beast-modell/` folder at the root of the current project (Replit, Claude Code, OpenClaw workspace, any git repo).
2. On hosts without a persistent project folder, the host's native memory (for example Perplexity Computer memory or Project files). Say which one is in use.
3. If neither is available, state that durable memory is not connected for this session.

To start a ledger, copy `assets/ledger/` from this skill into the project as `.beast-modell/`.

## Files

| File | Holds | Rule |
|---|---|---|
| `rules.md` | Project-specific rules and approved sources of record | User-approved only |
| `questions.md` | Recurring question recipes | Method only, never a cached answer |
| `decisions.md` | What was decided, by whom, when, why | Append-only |
| `observations.md` | Dated values (a sales total on a date) | History, never "current" |
| `feedback.md` | User feedback and corrections | Mark superseded entries |

## Entry format

Every entry starts with an id and an ISO date, and names its evidence:

```
### Q-0003 · 2026-11-17 · status: active
Evidence: user-stated | tool:<name> | source:<url or file> | query:<id>
```

Use `status: active`, `superseded by <id>`, or `needs review`. Ids are sequential per file (Q-, D-, O-, F-).
