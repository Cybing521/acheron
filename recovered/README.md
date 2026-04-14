# Recovered Python Sources

This directory contains the recovered Python artifacts for `Acheron` and `Mondo`.

## Layout

- `pyc/`
  Raw extracted bytecode files.
- `src/`
  Module-level decompilation output from `pycdc`.
- `snippets/`
  Method-level and nested code-object decompilation output from `pycdc -c -v 3.11`.
- `manifest.json`
  Summary of every recovered module, including stderr from `pycdc`.

## Practical Reading Order

- Start with `src/` for modules that decompile cleanly, especially auto-generated Qt UI modules.
- If a file in `src/` contains `# WARNING: Decompyle incomplete` or only shows `pass`, open the matching directory under `snippets/`.
- For large GUI/controller classes such as `mondo/main.py` or `acheron/gui/plotmain.py`, the `snippets/` directory is usually more useful than the raw module output.

## Regeneration

Run:

```bash
python3.11 tools/recover_python_sources.py
```

If you already have the `.pyc` extraction on disk and only want to rerun decompilation:

```bash
python3.11 tools/recover_python_sources.py --skip-extract
```
