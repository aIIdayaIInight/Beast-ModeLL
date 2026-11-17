# Install on Replit Agent

Sources: [Replit Agent Skills](https://docs.replit.com/features/agent/skills), [Agent Customization](https://docs.replit.com/features/agent/agent-customization), [replit.md](https://docs.replit.com/features/project-setup/replit-dot-md).

**One project:** copy `skills/beast-modell/` to `/.agents/skills/beast-modell/` in the Repl (turn on **Show Hidden Files**).

**Whole workspace:** **Workspace Settings → Customization → Skills → Create skill → Choose file or folder**, then select the `beast-modell` folder.

**Always on (recommended):** Replit loads skills only when it decides they are relevant. To make Beast-ModeLL apply to every message, add this line to the project's `replit.md`:

> Follow the Beast-ModeLL skill (`.agents/skills/beast-modell/SKILL.md`) on every task. Ledger: `.beast-modell/`.

Ledger: copy `skills/beast-modell/assets/ledger/` to `/.beast-modell/` in the Repl.
