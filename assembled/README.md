# Assembled Python Sources

This directory contains best-effort reconstructed `.py` files for `Acheron` and `Mondo`.

## What Is Here

- `src/`
  Reconstructed source tree.
- `manifest.json`
  Per-module assembly metadata.

## Assembly Modes

- `copied_clean`
  The module-level `pycdc` output looked clean, so the file was copied as-is.
- `reconstructed`
  The module-level output was incomplete, so the file was rebuilt from `.pyc` structure plus snippet/disassembly fallbacks.

## Current Totals

- modules copied clean: 62
- modules reconstructed: 96
- functions recovered from snippets: 899
- functions using disassembly fallback: 817

## Regeneration

```bash
python3.11 tools/assemble_recovered_sources.py
```
