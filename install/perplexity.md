# Install on Perplexity Computer

Source: [How to use Computer Skills](https://www.perplexity.ai/help-center/en/articles/13914413-how-to-use-computer-skills).

1. Run `scripts/package.sh`. It creates `dist/beast-modell.zip` with `SKILL.md` at the root.
2. In Perplexity Computer open **Plugins** → **Add custom** → **Upload plugin or skill** (older UI: **Customize → Skills → Create skill → Upload skill**).
3. Upload `dist/beast-modell.zip`.
4. Open the skill on the **Installed** tab and confirm the name and description.
5. For a single Perplexity Project, add it under **Project settings → Skills** instead.

Ledger: Perplexity has no project folder that persists like a repo, so the skill uses Perplexity's own memory or Project files and says which one it is using.
