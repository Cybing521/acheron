# acheron

`Acheron` / `Mondo` Windows 安装包的源码恢复与本地运行工程。

当前仓库不是原始官方源码，而是基于安装包中的 `Python 3.11` 字节码、资源文件和运行时资产，经过反编译、片段恢复、源码组装和手工修补后得到的可编辑工程。两个应用的 GUI 框架是 `PySide6`，不是 `PyQt`。

## 当前状态

- `Mondo` 已经可以通过恢复启动器完整导入到 GUI 入口模块。
- `Acheron` 也已经清理掉主要的旧冻结版裸导入，能完整导入到 `acheron.gui.__main__`。
- 当前仓库已经补了一套本机 `conda` 运行环境，规避了 macOS + Homebrew Python 上的 Qt platform plugin 问题。
- 仓库目前以“本地恢复、继续修复、后续自行重编译”为目标，暂不生成 exe。

## 目录说明

- `assembled/`
  组装后的可编辑源码、依赖清单与运行说明。
- `recovered/`
  模块级反编译结果、snippet 级恢复片段与清单。
- `tools/`
  反编译恢复、源码组装、运行时资产提取、启动器脚本。
- `analysis/`
  结构分析、补丁实验和逆向说明。
- `translations/`
  已抽取的 GUI 中文映射与字符串补丁资产。

## 快速开始

建议优先使用仓库内的 `conda` 环境。
这套脚本会用 `conda` 提供 `Python 3.11`，再用 `pip wheel` 安装 `PySide6`，以避开 macOS 上 conda 版 Qt plugin 的启动问题。

```bash
./tools/setup_conda_env.sh
./tools/run_recovered_app.sh mondo --probe-import
./tools/run_recovered_app.sh acheron --probe-import
./tools/run_smoke_qt_app.sh mondo
./tools/run_smoke_qt_app.sh acheron
```

也可以继续使用手动环境方式。建议使用 `Python 3.11`。

```bash
python3.11 -m venv .venv-recovered
source .venv-recovered/bin/activate
pip install -r assembled/requirements-local.txt
```

只验证导入链：

```bash
.venv-recovered/bin/python tools/bootstrap_recovered_app.py mondo --module mondo.__main__ --probe-import
.venv-recovered/bin/python tools/bootstrap_recovered_app.py acheron --module acheron.gui.__main__ --probe-import
```

尝试启动恢复版：

```bash
.venv-recovered/bin/python tools/bootstrap_recovered_app.py mondo
.venv-recovered/bin/python tools/bootstrap_recovered_app.py acheron
```

如果需要补原安装包里的运行时资产：

```bash
.venv-recovered/bin/python tools/extract_runtime_assets.py
```

更详细的依赖与运行说明见 `assembled/RUNNING.md`。

## 已知限制

- 反编译结果不是 100% 原始源码，部分复杂函数仍是 fallback / TODO 形式。
- 某些平台相关组件依赖 Windows 原生运行时或设备库，跨平台仅能做导入与结构验证。
- 当前仓库里的安装包和 PDF 手册不作为版本控制内容提交。

## 后续建议

- 优先在目标 Windows Python 3.11 环境验证 `Acheron` / `Mondo` GUI 真启动。
- 针对 fallback 较多的控制器模块继续做手工恢复。
- 稳定后再考虑重新打包。
