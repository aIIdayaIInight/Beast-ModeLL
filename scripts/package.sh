#!/usr/bin/env bash
# Builds dist/beast-modell.zip with SKILL.md at the zip root (Perplexity and Claude.ai upload format).
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/validate.py
mkdir -p dist && rm -f dist/beast-modell.zip
(cd skills/beast-modell && zip -qr ../../dist/beast-modell.zip . -x '.*')
echo "Built dist/beast-modell.zip"; unzip -l dist/beast-modell.zip | tail -n +1
