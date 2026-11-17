#!/usr/bin/env python3
"""Validate skills/beast-modell/SKILL.md against the Agent Skills spec (agentskills.io/specification)."""
import re, sys, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
skill = root / "skills" / "beast-modell"
text = (skill / "SKILL.md").read_text()
errors = []
m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
if not m:
    sys.exit("FAIL: missing YAML frontmatter")
front, body = m.groups()
fields = dict(re.findall(r"^([a-z-]+):\s*(.*)$", front, re.M))
name, desc = fields.get("name", ""), fields.get("description", "")
if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
    errors.append(f"name invalid: {name!r}")
if name != skill.name:
    errors.append(f"name {name!r} must match folder {skill.name!r}")
if any(w in name for w in ("anthropic", "claude")):
    errors.append("name uses a reserved word")
if not 1 <= len(desc) <= 1024 or "<" in desc:
    errors.append(f"description length {len(desc)} or contains '<'")
if len(body.splitlines()) > 500:
    errors.append("body over 500 lines")
for link in re.findall(r"\]\(((?:references|assets)/[^)]+)\)", body):
    if not (skill / link).exists():
        errors.append(f"broken link: {link}")
files = [p for p in skill.rglob("*") if p.is_file()]
if len(files) > 100:
    errors.append(f"{len(files)} files; Perplexity allows 100")
if errors:
    print("FAIL"); [print(" -", e) for e in errors]; sys.exit(1)
print(f"OK: {name} | description {len(desc)} chars | body {len(body.splitlines())} lines | {len(files)} files")
