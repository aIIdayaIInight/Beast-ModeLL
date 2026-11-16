# Project scopes

Beast-ModeLL is the shared rulebook for every project. Each project keeps its own memory lane so facts, decisions, and credentials never bleed across projects.

## How scopes work

- The Golden Rulez and `AGENTS.md` apply to every project equally.
- Each project has a `project_id` that must be attached to every memory record (see the root README memory contract).
- Retrieval is limited to the active project plus the `shared` scope. Cross-project retrieval is denied unless the user explicitly approves it for a specific task.
- Each project file lists its surfaces, approved sources of record, and open questions. Anything not confirmed by the user or a verified source stays under **To confirm** — never guessed.

## Registered projects

| project_id | Project | Surfaces (user-stated) | File |
|---|---|---|---|
| `shared` | Cross-project rules and preferences | Golden Rulez, user preferences | this file |
| `archangel` | Archangel projects | To confirm: which projects are in scope | [archangel.md](archangel.md) |
| `lorneslines` | LornesLines | lorneslines.com site, app | [lorneslines.md](lorneslines.md) |
| `harbor-village` | Harbor Village Florida | website, Google Business Profile, social | [harbor-village.md](harbor-village.md) |
| `comboword` | ComboWord | comboword.com site, app | [comboword.md](comboword.md) |

New projects ("and then some") are added by copying [`_template.md`](_template.md) and registering them in this table.

## Status

These are scope definitions only. No memory backend, retrieval service, or agent integration is connected yet.
