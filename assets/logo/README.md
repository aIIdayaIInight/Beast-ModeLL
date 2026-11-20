# Beast-ModeLL logo

Built with [GIMP](https://www.gimp.org/) 3.2.2 using a Python-Fu batch script.

| File | Use |
|---|---|
| `beast-modell-banner.png` | README header (2000x1000, dark pattern background) |
| `beast-modell-sticker.png` | Transparent sticker, for decks, sites, avatars |
| `beast-modell-logo.xcf` | Layered GIMP source: text, gold LL, claw print, grid, claw marks, sticker, shadow |
| `build_logo.py` | Script that regenerates all three files |

## Rebuild

1. Install fonts: [Rubik Wet Paint](https://fonts.google.com/specimen/Rubik+Wet+Paint) (SIL Open Font License) and [Permanent Marker](https://fonts.google.com/specimen/Permanent+Marker) (Apache 2.0).
2. From this folder run:

```bash
gimp-console -i --quit --batch-interpreter=python-fu-eval -b "exec(open('build_logo.py').read())"
```

Colors: black `#0a0a0a`, Golden Rulez gold `#d4a017` (gradient `#ffd95a` to `#a8780a` on the LL), white sticker. The O carries a three-slash claw print instead of a paw. Original design; the style reference was a user-supplied "Beast Mode" sticker.
