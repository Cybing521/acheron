# Running The Recovered Apps

## What Is In Place

- `src/acheron/`
  Recovered Acheron source tree, plus recovered `asphodel`, `hyperborea`, and `setproctitle` support packages.
- `src/mondo/`
  Recovered Mondo source tree, plus recovered `asphodel` and `hyperborea` support packages.
- `requirements-acheron.txt`
  Best-effort runtime dependency set for a clean Python 3.11 environment.
- `requirements-mondo.txt`
  Best-effort runtime dependency set for a clean Python 3.11 environment.
- `requirements-local.txt`
  Combined local-development dependency set that works in a single Python 3.11 virtualenv.

## Bootstrapping

Use the helper so the recovered tree behaves more like the original frozen layout:

```bash
python3.11 -m venv .venv-recovered
.venv-recovered/bin/pip install -r assembled/requirements-local.txt
.venv-recovered/bin/python tools/bootstrap_recovered_app.py acheron --probe-import
.venv-recovered/bin/python tools/bootstrap_recovered_app.py mondo --probe-import
```

To actually launch:

```bash
.venv-recovered/bin/python tools/bootstrap_recovered_app.py acheron
.venv-recovered/bin/python tools/bootstrap_recovered_app.py mondo
```

The bootstrap helper also configures `QT_PLUGIN_PATH`, `QT_QPA_PLATFORM_PLUGIN_PATH`, and `DYLD_FRAMEWORK_PATH` (on macOS) from the installed `PySide6` wheel so the GUI runtime can find its Qt platform plugins.

## Recommended Local macOS Setup

If the Homebrew/PyPI stack still fails on macOS because Qt cannot initialize a platform plugin, use the repository-local conda environment instead:

```bash
./tools/setup_conda_env.sh
./tools/run_recovered_app.sh mondo --probe-import
./tools/run_recovered_app.sh acheron --probe-import
./tools/run_recovered_app.sh mondo
./tools/run_recovered_app.sh acheron
```

`run_recovered_app.sh` uses `.conda-recovered/bin/python` directly and pins `MPLCONFIGDIR` to a repository-local cache so `matplotlib` does not rebuild fonts into a random user cache directory on first run.
`setup_conda_env.sh` keeps `Python 3.11` in conda and prefers a locally installed `PySide6 6.10.x` when one already exists; otherwise it falls back to pip wheels. It also mirrors `PySide6/Qt/plugins` into a visible `qt-runtime/plugins` directory so macOS Qt does not miss platform plugins inside the hidden `.conda-recovered` path. That avoids the older Cocoa plugin startup aborts we saw with `6.7.x` and reduces repeated multi-hundred-megabyte downloads.

For a reproducible startup smoke test that auto-quits after a short delay:

```bash
./tools/run_smoke_qt_app.sh mondo
./tools/run_smoke_qt_app.sh acheron
```

For a non-GUI backend smoke test that validates the Acheron dispatcher/connectivity lifecycle:

```bash
./.conda-recovered/bin/python tools/smoke_acheron_backend.py
```

## Runtime Assets

The original installers ship a few non-Python runtime assets that are not embedded in the recovered source tree:

- `Acheron`
  `build_info.txt`, `botodata/`, `asphodel/lib64/*.dll`, and `setproctitle._setproctitle.cp311-win_amd64.pyd`
- `Mondo`
  `build_info.txt` and `asphodel/lib64/*.dll`

Extract them with:

```bash
python3.11 tools/extract_runtime_assets.py acheron mondo
```

They will be written under `runtime_support/<app>/...`. The bootstrap script automatically points `AWS_DATA_PATH` and `AWS_CA_BUNDLE` at `runtime_support/acheron/botodata` when it exists.

## Current Limitation

The recovered source tree is now importable and syntax-valid, but full end-to-end GUI verification still depends on a Windows Python 3.11 runtime with the matching native DLLs and wheels available.
