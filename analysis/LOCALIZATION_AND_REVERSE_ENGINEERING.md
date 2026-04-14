# Acheron / Mondo Reverse Engineering Notes

## What Was Confirmed

- Both setup files are `Inno Setup 6.3.x` installers.
- `Acheron` installs a Python 3.11 application with business modules under `data/{app}/lib/acheron/*.pyc`.
- `Mondo` installs a Python 3.11 application whose business modules are mainly inside `data/{app}/lib/library.zip` under `mondo/*` and `hyperborea/*`.
- The installer script is minimal and only handles self-deletion after install. There is no custom multilingual setup logic embedded there.

## Localization Strategy

- Installer UI: still English-only; repacking the full setup EXE would require rebuilding an Inno installer or patching message resources.
- Application UI: feasible to localize by patching Python 3.11 `.pyc` string constants in the GUI modules.
- This workspace now includes:
  - `tools/extract_pyc_strings.py` to extract candidate strings from `.pyc`
  - `tools/patch_pyc_strings.py` to rewrite string constants in `.pyc`
  - `translations/acheron_gui_zh.json` and `translations/mondo_gui_zh.json` as starter Chinese mappings

## Source Recovery Strategy

- Traditional decompilers like `decompyle3` and `uncompyle6` detect these files as Python 3.11 but do not support full decompilation for this bytecode version.
- Source recovery is still partially feasible because:
  - module names
  - package structure
  - embedded filenames
  - string constants
  - bytecode disassembly
  are all available right now.
- For fuller recovery of `.py` source, the next toolchain to test should be a Python 3.11-capable decompiler such as `pycdc` or a modern AST/LLM-assisted workflow.

## Useful Commands

```bash
~/Library/Python/3.9/bin/ef Acheron_Setup_Win64_c7f9da5e7a33a154d737fdffa9887c9ba5033f67.exe | \
  ~/Library/Python/3.9/bin/xtinno -l

python3.11 tools/extract_pyc_strings.py analysis/mondo_pyc/ui_main.pyc

python3.11 tools/patch_pyc_strings.py \
  --mapping translations/mondo_gui_zh.json \
  analysis/mondo_pyc/ui_main.pyc \
  analysis/patched/mondo/ui_main.pyc
```
