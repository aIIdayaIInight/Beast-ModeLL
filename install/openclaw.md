# Install on OpenClaw

Sources: [OpenClaw skills](https://docs.openclaw.ai/tools/skills), [Skills CLI](https://docs.openclaw.ai/cli/skills).

OpenClaw's git install expects `SKILL.md` at the repository root, so install from a local clone:

```bash
git clone https://github.com/aIIdayaIInight/Beast-ModeLL.git
openclaw skills install ./Beast-ModeLL/skills/beast-modell            # active workspace
openclaw skills install ./Beast-ModeLL/skills/beast-modell --global   # all agents
openclaw skills check                                                  # confirm it is ready and visible
```

Ledger: copy `skills/beast-modell/assets/ledger/` to `<workspace>/.beast-modell/`.
