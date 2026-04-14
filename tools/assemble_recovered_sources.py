#!/usr/bin/env python3.11
from __future__ import annotations

import argparse
import dis
import inspect
import json
import marshal
import re
import shutil
import types
from dataclasses import asdict, dataclass
from pathlib import Path

PYC_HEADER_SIZE = 16
ROOT = Path(__file__).resolve().parents[1]
RECOVERED_ROOT = ROOT / "recovered"
PYC_ROOT = RECOVERED_ROOT / "pyc"
SRC_ROOT = RECOVERED_ROOT / "src"
SNIPPET_ROOT = RECOVERED_ROOT / "snippets"

ASSEMBLED_ROOT = ROOT / "assembled"
ASSEMBLED_SRC_ROOT = ASSEMBLED_ROOT / "src"
ASSEMBLED_MANIFEST = ASSEMBLED_ROOT / "manifest.json"
ASSEMBLED_README = ASSEMBLED_ROOT / "README.md"

QUALNAME_CLEAN_RE = re.compile(r"[^A-Za-z0-9_.-]+")
CLASS_DEF_RE = re.compile(r"^class\s+([A-Za-z_][A-Za-z0-9_]*)(?:\((.*?)\))?:")
MAX_DISASSEMBLY_LINES = 80
SUSPICIOUS_SNIPPET_RE = re.compile(
    r"\bNone\.(?!__class__)"
    r"|\bNone\s*\("
    r"|\bNone\["
    r"|\bNone\s*(==|!=|<=|>=|<|>|in\b)"
    r"|\bnot\s+None\b"
)
SUSPICIOUS_SOURCE_RE = re.compile(
    SUSPICIOUS_SNIPPET_RE.pattern
    + r"|<NODE:12>"
    + r"|^from\s+\s+import\s+"
    + r"|^#\s*WARNING:\s*Decompyle incomplete",
    re.M,
)
FORCE_RECONSTRUCT_MODULES: set[str] = set()
MODULE_TEXT_REPLACEMENTS: dict[str, list[tuple[str, str]]] = {
    "acheron:acheron/__init__.py": [
        (
            "import setproctitle",
            "\n".join(
                [
                    "try:",
                    "    import setproctitle",
                    "except ImportError:",
                    "    class _SetProcTitleShim:",
                    "        @staticmethod",
                    "        def setproctitle(_title):",
                    "            return None",
                    "",
                    "    setproctitle = _SetProcTitleShim()",
                ]
            ),
        ),
        (
            "\n".join(
                [
                    "try:",
                    "    from version import version as __version__",
                    "except ImportError:",
                    "    __version__ = 'UNKNOWN'",
                ]
            ),
            "\n".join(
                [
                    "try:",
                    "    from .version import version as __version__",
                    "except ImportError:",
                    "    try:",
                    "        from version import version as __version__",
                    "    except ImportError:",
                    "        __version__ = 'UNKNOWN'",
                ]
            ),
        ),
    ],
    "acheron:acheron/gui/__main__.py": [
        ("from device_process.proxy import DeviceProxyManager", "from ..device_process.proxy import DeviceProxyManager"),
        ("from plotmain import PlotMainWindow", "from .plotmain import PlotMainWindow"),
    ],
    "acheron:acheron/logging.py": [
        ("import logging.handlers as logging", "import logging\nimport logging.handlers"),
    ],
    "acheron:hyperborea/namedprocess.py": [
        ("import multiprocessing.spawn as multiprocessing", "import multiprocessing"),
    ],
    "mondo:mondo/__init__.py": [
        ("from export_script import matplotlib_wrapper as matplotlib", "from .export_script import matplotlib_wrapper as matplotlib"),
        (
            "\n".join(
                [
                    "try:",
                    "    from version import version as __version__",
                    "except ImportError:",
                    "    __version__ = 'UNKNOWN'",
                ]
            ),
            "\n".join(
                [
                    "try:",
                    "    from .version import version as __version__",
                    "except ImportError:",
                    "    try:",
                    "        from version import version as __version__",
                    "    except ImportError:",
                    "        __version__ = 'UNKNOWN'",
                ]
            ),
        ),
        (
            "\n".join(
                [
                    "# INVALID FROM DECOMPILER: if __name__ == '__main__':",
                    "# INVALID FROM DECOMPILER:     from  import __main__",
                    "# INVALID FROM DECOMPILER:     __main__.main()",
                    "# INVALID FROM DECOMPILER:     return None",
                ]
            ),
            "\n".join(
                [
                    "if __name__ == '__main__':",
                    "    from . import __main__",
                    "    __main__.main()",
                ]
            ),
        ),
    ],
    "mondo:mondo/__main__.py": [
        ("import logging.handlers as logging", "import logging\nimport logging.handlers"),
        ("from main import MondoMainWindow", "from .main import MondoMainWindow"),
        ("if not sys.stdout or sys.stderr:", "if not sys.stdout or not sys.stderr:"),
    ],
    "mondo:mondo/export_script.py": [
        ("ignored_types = builtins.__dict__.values()()", "ignored_types = list(builtins.__dict__.values())"),
    ],
}
MANUAL_FUNCTION_OVERRIDES: dict[tuple[str, str], str] = {
    (
        "acheron:hyperborea/namedprocess.py",
        "NamedProcess.__init__",
    ): "\n".join(
        [
            "self.title = f'{name} {description}'",
            "self.executable = None",
            "if sys.platform == 'win32':",
            "    with lock:",
            "        original_name = multiprocessing.spawn.get_executable()",
            "    new_name = os.path.abspath(os.path.join(os.path.dirname(original_name), name + '.exe'))",
            "    if os.path.isfile(new_name):",
            "        self.executable = new_name",
            "super().__init__(name=name, **kwargs)",
            "return None",
        ]
    ),
    (
        "acheron:hyperborea/namedprocess.py",
        "NamedProcess.start",
    ): "\n".join(
        [
            "if self.executable:",
            "    with lock:",
            "        old_name = multiprocessing.spawn.get_executable()",
            "        try:",
            "            multiprocessing.spawn.set_executable(self.executable)",
            "            super().start()",
            "        finally:",
            "            multiprocessing.spawn.set_executable(old_name)",
            "    return None",
            "super().start()",
            "return None",
        ]
    ),
    (
        "acheron:hyperborea/namedprocess.py",
        "NamedProcess.run",
    ): "\n".join(
        [
            "if setproctitle:",
            "    setproctitle.setproctitle(self.title)",
            "super().run()",
            "return None",
        ]
    ),
    (
        "mondo:mondo/export_script.py",
        "is_ignored_type",
    ): "\n".join(
        [
            "if isinstance(value, QtCore.QObject):",
            "    return True",
            "for t in ignored_types:",
            "    if type(value) == t:",
            "        return True",
            "return False",
        ]
    ),
    (
        "mondo:mondo/export_script.py",
        "CommandList.__init__",
    ): "\n".join(
        [
            "self.plotdata = {}",
            "self._index = 0",
            "if not setup_commands:",
            "    self.append('import matplotlib')",
            "    self.append('import numpy')",
            "    self.append('from PySide6 import QtGui')",
            "    self.append('')",
            "    return None",
            "self.extend(setup_commands)",
            "self.append('')",
            "self.append(\"plotdata = numpy.load(__file__ + '.npz')\")",
            "return None",
        ]
    ),
    (
        "mondo:mondo/export_script.py",
        "CommandList.get_string",
    ): "\n".join(
        [
            "if isinstance(value, numpy.ndarray):",
            "    i = 'array_{}'.format(self._index)",
            "    self._index += 1",
            "    self.plotdata[i] = value",
            "    return \"plotdata['{}']\".format(i)",
            "return repr(value)",
        ]
    ),
    (
        "mondo:mondo/export_script.py",
        "CommandList.output",
    ): "\n".join(
        [
            "datafile = scriptfile + '.npz'",
            "logger.debug('Writing script to {}'.format(scriptfile))",
            "with open(scriptfile, 'wt', encoding='utf_8') as f:",
            "    for v in self:",
            "        s = str(v)",
            "        if s == 'fig.show()':",
            "            s = 'plt.show()'",
            "        f.write(s)",
            "        f.write('\\n')",
            "logger.debug('Writing script data to {}'.format(datafile))",
            "if self.plotdata:",
            "    numpy.savez(datafile, **self.plotdata)",
            "return None",
        ]
    ),
    (
        "mondo:mondo/export_script.py",
        "Wrapper.__getattribute__",
    ): "\n".join(
        [
            "wrapped = object.__getattribute__(self, '_wrapped')",
            "name = object.__getattribute__(self, '_name')",
            "cmd_list = object.__getattribute__(self, '_cmd_list')",
            "orig_attr = wrapped.__getattribute__(attr)",
            "if callable(orig_attr):",
            "    def wrapped_func(*args, **kwargs):",
            "        new_name = AttributeCommand(cmd_list, name, attr)",
            "        result = orig_attr(*args, **kwargs)",
            "        cmd_list.append(CallCommand(cmd_list, name, attr, *args, **kwargs))",
            "        if is_ignored_type(result):",
            "            return result",
            "        return Wrapper(result, new_name, cmd_list)",
            "",
            "    return wrapped_func",
            "if is_ignored_type(orig_attr):",
            "    return orig_attr",
            "new_name = AttributeCommand(cmd_list, name, attr)",
            "return Wrapper(orig_attr, new_name, cmd_list)",
        ]
    ),
    (
        "mondo:mondo/export_script.py",
        "Wrapper.__getitem__",
    ): "\n".join(
        [
            "wrapped = object.__getattribute__(self, '_wrapped')",
            "name = object.__getattribute__(self, '_name')",
            "cmd_list = object.__getattribute__(self, '_cmd_list')",
            "new_name = GetItemCommand(cmd_list, name, key)",
            "value = wrapped.__getitem__(key)",
            "if is_ignored_type(value):",
            "    return value",
            "return Wrapper(value, new_name, cmd_list)",
        ]
    ),
    (
        "acheron:acheron/logging.py",
        "GUILogFormatter.__init__",
    ): "\n".join(
        [
            "super().__init__(",
            "    '[%(asctime)s] %(optdevice)s%(optlevel)s%(message)s',",
            "    '%Y-%m-%dT%H:%M:%SZ',",
            "    defaults={'optlevel': ''},",
            ")",
            "return None",
        ]
    ),
    (
        "acheron:acheron/logging.py",
        "GUILogFormatter.format",
    ): "\n".join(
        [
            "if record.levelno >= logging.WARNING:",
            "    record.optlevel = record.levelname + ' - '",
            "s = super().format(record)",
            "lines = s.split('\\n')",
            "if len(lines) <= 1:",
            "    return s",
            "return lines[0] + ' | ' + lines[-1]",
        ]
    ),
    (
        "acheron:acheron/logging.py",
        "_clean_fault_dir",
    ): "\n".join(
        [
            "with os.scandir(fault_dir) as it:",
            "    for entry in it:",
            "        if not entry.name.endswith('.log') or not entry.is_file():",
            "            continue",
            "        try:",
            "            if entry.stat().st_size == 0:",
            "                os.unlink(os.path.join(fault_dir, entry.name))",
            "        except OSError:",
            "            continue",
            "return None",
        ]
    ),
    (
        "acheron:acheron/logging.py",
        "setup_logging",
    ): "\n".join(
        [
            "def my_excepthook(exctype=None, value=None, traceback=None):",
            "    exc_info = (exctype, value, traceback)",
            "    logger.error('Uncaught Exception', exc_info=exc_info)",
            "",
            "sys.excepthook = my_excepthook",
            "logdir = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.StandardLocation.AppLocalDataLocation)",
            "logfile = os.path.join(logdir, 'main.log')",
            "os.makedirs(logdir, exist_ok=True)",
            "optdevice_filter = OptionalDeviceStringFilter('[%s] ', '')",
            "file_log_handler = logging.handlers.RotatingFileHandler(",
            "    logfile,",
            "    maxBytes=int(1e+07),",
            "    backupCount=9,",
            "    encoding='utf-8',",
            ")",
            "file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(optdevice)s%(message)s')",
            "file_formatter.default_time_format = '%Y-%m-%dT%H:%M:%S'",
            "file_formatter.default_msec_format = '%s,%03dZ'",
            "file_formatter.converter = time.gmtime",
            "file_log_handler.addFilter(optdevice_filter)",
            "file_log_handler.setFormatter(file_formatter)",
            "file_log_handler.setLevel(logging.DEBUG)",
            "root_logger = logging.getLogger()",
            "root_logger.addHandler(file_log_handler)",
            "root_logger.setLevel(logging.DEBUG)",
            "if console:",
            "    console_formatter = logging.Formatter('[%(asctime)s] %(optdevice)s%(message)s')",
            "    console_formatter.default_time_format = '%Y-%m-%dT%H:%M:%S'",
            "    console_formatter.default_msec_format = '%s,%03dZ'",
            "    console_formatter.converter = time.gmtime",
            "    console_handler = logging.StreamHandler()",
            "    console_handler.addFilter(optdevice_filter)",
            "    console_handler.setFormatter(console_formatter)",
            "    console_handler.setLevel(logging.INFO)",
            "    root_logger.addHandler(console_handler)",
            "else:",
            "    from acheron.gui.gui_log import GUILogHandler",
            "",
            "    nodevice_filter = OptionalDeviceStringFilter('%.0s', '[*] ')",
            "    gui_formatter = GUILogFormatter()",
            "    gui_formatter.converter = time.gmtime",
            "    gui_handler = GUILogHandler()",
            "    gui_handler.addFilter(nodevice_filter)",
            "    gui_handler.setFormatter(gui_formatter)",
            "    gui_handler.setLevel(logging.INFO)",
            "    root_logger.addHandler(gui_handler)",
            "pyusb_logger = logging.getLogger('usb')",
            "pyusb_logger.propagate = False",
            "logging.getLogger('boto3').setLevel(logging.INFO)",
            "logging.getLogger('botocore').setLevel(logging.INFO)",
            "logging.getLogger('s3transfer').setLevel(logging.INFO)",
            "logging.getLogger('urllib3').setLevel(logging.INFO)",
            "logging.getLogger('pymodbus').setLevel(logging.INFO)",
            "fault_dir = os.path.join(logdir, 'fault')",
            "os.makedirs(fault_dir, exist_ok=True)",
            "dt = datetime.datetime.now(tz=datetime.timezone.utc)",
            "dt_str = dt.strftime('fault_%Y%m%dT%H%M%SZ.log')",
            "fault_filename = os.path.join(fault_dir, dt_str)",
            "_clean_fault_dir(fault_dir)",
            "fault_file = open(fault_filename, 'wt')",
            "faulthandler.enable(fault_file)",
            "return None",
        ]
    ),
    (
        "acheron:asphodel/__init__.py",
        "AsphodelNativeDevice.get_strain_bridge_values",
    ): "\n".join(
        [
            "array = (c_float * 5)()",
            "self.lib.lib.asphodel_get_strain_bridge_values(channel_info, bridge_index, array)",
            "return BridgeValues(*array)",
        ]
    ),
    (
        "acheron:asphodel/__init__.py",
        "AsphodelNativeDevice.get_accel_self_test_limits",
    ): "\n".join(
        [
            "array = (c_float * 6)()",
            "self.lib.lib.asphodel_get_accel_self_test_limits(channel_info, array)",
            "return SelfTestLimits(*array)",
        ]
    ),
    (
        "mondo:asphodel/__init__.py",
        "AsphodelNativeDevice.get_strain_bridge_values",
    ): "\n".join(
        [
            "array = (c_float * 5)()",
            "self.lib.lib.asphodel_get_strain_bridge_values(channel_info, bridge_index, array)",
            "return BridgeValues(*array)",
        ]
    ),
    (
        "mondo:asphodel/__init__.py",
        "AsphodelNativeDevice.get_accel_self_test_limits",
    ): "\n".join(
        [
            "array = (c_float * 6)()",
            "self.lib.lib.asphodel_get_accel_self_test_limits(channel_info, array)",
            "return SelfTestLimits(*array)",
        ]
    ),
    (
        "mondo:mondo/__main__.py",
        "main",
    ): "\n".join(
        [
            "multiprocessing.freeze_support()",
            "if main_is_frozen() and sys.platform == 'win32':",
            "    myappid = 'com.sprocktech.mondo.' + mondo.__version__",
            "    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)",
            "if not sys.stdout or not sys.stderr:",
            "    sys.stdout = open(os.devnull)",
            "    sys.stderr = open(os.devnull)",
            "app = QtWidgets.QApplication(sys.argv)",
            "app.setApplicationName('Mondo')",
            "app.setOrganizationDomain('suprocktech.com')",
            "app.setOrganizationName('Suprock Tech')",
            "QtGui.QIcon.setThemeName('suprock')",
            "icon = QtGui.QIcon()",
            "icon_reader = QtGui.QImageReader(':/mondo.ico')",
            "pixmap = QtGui.QPixmap.fromImage(icon_reader.read())",
            "icon.addPixmap(pixmap)",
            "if not icon_reader.jumpToNextImage():",
            "    pass",
            "app.setWindowIcon(icon)",
            "QtCore.QSettings.setDefaultFormat(QtCore.QSettings.Format.IniFormat)",
            "app.setStyleSheet('QMessageBox { messagebox-text-interaction-flags: 5; }')",
            "app.setApplicationVersion(mondo.__version__)",
            "setup_logging()",
            "logger.info('Mondo started (Version {})'.format(mondo.__version__))",
            "app.setStyleSheet('QMessageBox { messagebox-text-interaction-flags: 5; }')",
            "matplotlib.rc('font', size=17)",
            "mainwin = MondoMainWindow()",
            "mainwin.show()",
            "app.exec()",
            "logger.info('Mondo finished')",
            "return None",
        ]
    ),
    (
        "acheron:acheron/__init__.py",
        "shutdown_signal",
    ): "\n".join(
        [
            "from PySide6 import QtCore",
            "QtCore.QCoreApplication.quit()",
            "return None",
        ]
    ),
    (
        "acheron:acheron/__init__.py",
        "main_init",
    ): "\n".join(
        [
            "multiprocessing.freeze_support()",
            "try:",
            "    multiprocessing.set_start_method('spawn')",
            "except RuntimeError:",
            "    pass",
            "setproctitle.setproctitle(main_process_title)",
            "if main_is_frozen():",
            "    cacert = os.path.join(os.path.dirname(sys.executable), 'botodata', 'cacert.pem')",
            "    os.environ['AWS_CA_BUNDLE'] = cacert",
            "    botodata = os.path.join(os.path.dirname(sys.executable), 'botodata')",
            "    os.environ['AWS_DATA_PATH'] = botodata",
            "elif sys.platform == 'win32':",
            "    myappid = 'com.sprocktech.' + main_process_title + '.' + __version__",
            "    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)",
            "if not sys.stdout or not sys.stderr:",
            "    sys.stdout = open(os.devnull)",
            "    sys.stderr = open(os.devnull)",
            "from PySide6 import QtCore",
            "QtCore.QSettings.setDefaultFormat(QtCore.QSettings.Format.IniFormat)",
            "signal.signal(signal.SIGINT, shutdown_signal)",
            "signal.signal(signal.SIGTERM, shutdown_signal)",
            "return None",
        ]
    ),
    (
        "acheron:acheron/build_info.py",
        "_load_values",
    ): "\n".join(
        [
            "is_frozen = getattr(sys, 'frozen', False)",
            "if not is_frozen:",
            "    return None",
            "main_dir = os.path.dirname(sys.executable)",
            "build_info_filename = os.path.join(main_dir, 'build_info.txt')",
            "try:",
            "    with open(build_info_filename, 'r', encoding='utf-8') as f:",
            "        lines = f.readlines()",
            "    branch_name = lines[0].strip()",
            "    commit_hash = lines[1].strip()",
            "    build_key = lines[2].strip()",
            "    build_date = lines[3].strip()",
            "    return (branch_name, commit_hash, build_key, build_date)",
            "except Exception:",
            "    logger.exception('Could not read build_info.txt')",
            "    return None",
        ]
    ),
    (
        "acheron:acheron/device_process/rgb_manager.py",
        "RGBManager.connected_locked",
    ): "\n".join(
        [
            "self.device_info = device_info",
            "if self.auto_rgb:",
            "    if device_info.supports_radio:",
            "        self.set_rgb_locked(0, (0, 255, 255))",
            "        return None",
            "    self.set_rgb_locked(0, (0, 0, 255))",
            "    return None",
        ]
    ),
    (
        "acheron:acheron/device_process/rgb_manager.py",
        "RGBManager.streaming_locked",
    ): "\n".join(
        [
            "if self.auto_rgb and self.device_info:",
            "    if self.device_info.supports_radio:",
            "        return None",
            "    self.set_rgb_locked(0, (0, 255, 0))",
            "    return None",
            "return None",
        ]
    ),
}
MANUAL_SIGNATURE_OVERRIDES: dict[tuple[str, str], str] = {
    ("acheron:acheron/device_process/rgb_manager.py", "RGBManager.set_rgb_locked"): "self, index, values, instant=False",
}


@dataclass
class AssemblyStats:
    package: str
    pyc_path: str
    source_path: str
    assembled_path: str
    mode: str
    top_level_items: int
    snippet_functions: int
    fallback_functions: int


@dataclass
class ClassMetadata:
    name: str
    bases: list[str]
    decorators: list[str]


@dataclass
class ClassBuild:
    name: str
    code: types.CodeType
    bases: list[str]
    decorators: list[str]


def ensure_clean_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def load_code(path: Path) -> types.CodeType:
    data = path.read_bytes()
    return marshal.loads(data[PYC_HEADER_SIZE:])


def iter_child_codes(code: types.CodeType) -> list[types.CodeType]:
    return [const for const in code.co_consts if isinstance(const, types.CodeType)]


def sanitize_qualname(name: str) -> str:
    return QUALNAME_CLEAN_RE.sub("_", name).strip("._") or "code"


def parse_class_bases(source_text: str) -> dict[str, str]:
    bases: dict[str, str] = {}
    for line in source_text.splitlines():
        match = CLASS_DEF_RE.match(line.strip())
        if match:
            bases[match.group(1)] = (match.group(2) or "").strip()
    return bases


def extract_preamble(source_text: str) -> str:
    lines: list[str] = []
    for line in source_text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("class ") or stripped.startswith("def ") or stripped.startswith("# WARNING:"):
            break
        lines.append(line)
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines)


def resolve_relative_import(source_path: Path, target: str) -> str | None:
    current_dir = source_path.parent
    for depth_up, directory in enumerate([current_dir, *current_dir.parents]):
        if directory.name == "src":
            break
        module_file = directory / f"{target}.py"
        package_dir = directory / target / "__init__.py"
        if module_file.exists() or package_dir.exists() or target == "__version__":
            return "." * (depth_up + 1)
    return None


def repair_invalid_preamble_line(line: str, source_path: Path) -> str:
    prefix = "# INVALID FROM DECOMPILER: "
    payload = line[len(prefix) :] if line.startswith(prefix) else line
    from_match = re.match(r"from\s+\s+import\s+([A-Za-z_][A-Za-z0-9_]*)(.*)$", payload)
    if from_match:
        target = from_match.group(1)
        rest = from_match.group(2)
        dots = resolve_relative_import(source_path, target)
        if dots:
            return f"from {dots} import {target}{rest}"
    return payload


def line_is_block_opener(line: str) -> bool:
    stripped = line.strip()
    return bool(
        stripped
        and (
            stripped.endswith(":")
            or stripped.startswith(("elif ", "else:", "except ", "except:", "finally:"))
        )
    )


def line_is_block_continuation(line: str) -> bool:
    return bool(line.startswith((" ", "\t"))) or line.strip().startswith(
        ("elif ", "else:", "except ", "except:", "finally:")
    )


def sanitize_preamble(preamble: str, source_path: Path) -> str:
    original_lines = preamble.splitlines()
    sanitized: list[str] = []
    index = 0
    while index < len(original_lines):
        raw_line = original_lines[index]
        candidate = repair_invalid_preamble_line(raw_line, source_path)

        if line_is_block_opener(candidate):
            raw_group = [raw_line]
            candidate_group = [candidate]
            index += 1
            while index < len(original_lines):
                next_raw = original_lines[index]
                next_candidate = repair_invalid_preamble_line(next_raw, source_path)
                if not line_is_block_continuation(next_candidate):
                    break
                raw_group.append(next_raw)
                candidate_group.append(next_candidate)
                index += 1

            trial = "\n".join(sanitized + candidate_group) + "\n"
            try:
                compile(trial, "<assembled-preamble>", "exec")
            except SyntaxError:
                sanitized.extend(f"# INVALID FROM DECOMPILER: {line}" for line in raw_group)
            else:
                sanitized.extend(candidate_group)
            continue

        trial = "\n".join(sanitized + [candidate]) + "\n"
        try:
            compile(trial, "<assembled-preamble>", "exec")
        except SyntaxError:
            sanitized.append(f"# INVALID FROM DECOMPILER: {raw_line}")
        else:
            sanitized.append(candidate)
        index += 1
    return "\n".join(sanitized)


def source_text_is_compilable(source_text: str) -> bool:
    try:
        compile(source_text, "<recovered-source>", "exec")
    except SyntaxError:
        return False
    return True


def source_text_is_trustworthy(source_text: str) -> bool:
    return source_text_is_compilable(source_text) and not bool(SUSPICIOUS_SOURCE_RE.search(source_text))


def apply_module_text_replacements(module_key: str, source_text: str) -> str:
    custom_only_modules = {
        "acheron:acheron/__init__.py",
        "acheron:hyperborea/__init__.py",
        "mondo:mondo/__init__.py",
        "mondo:mondo/__main__.py",
    }
    if module_key not in custom_only_modules:
        for old, new in MODULE_TEXT_REPLACEMENTS.get(module_key, []):
            source_text = source_text.replace(old, new)
    if module_key == "acheron:acheron/__init__.py":
        source_text = source_text.replace(
            "import setproctitle",
            "\n".join(
                [
                    "try:",
                    "    import setproctitle",
                    "except ImportError:",
                    "    class _SetProcTitleShim:",
                    "        @staticmethod",
                    "        def setproctitle(_title):",
                    "            return None",
                    "",
                    "    setproctitle = _SetProcTitleShim()",
                ]
            ),
        )
        source_text = source_text.replace(
            "\n".join(
                [
                    "try:",
                    "    from version import version as __version__",
                    "except ImportError:",
                    "    __version__ = 'UNKNOWN'",
                ]
            ),
            "\n".join(
                [
                    "try:",
                    "    from .version import version as __version__",
                    "except ImportError:",
                    "    try:",
                    "        from version import version as __version__",
                    "    except ImportError:",
                    "        __version__ = 'UNKNOWN'",
                ]
            ),
        )
        source_text = source_text.replace(
            "\n".join(
                [
                    "def shutdown_signal(*args):",
                    "    QtCore = QtCore",
                    "    import PySide6",
                    "    QtCore.QCoreApplication.quit()",
                ]
            ),
            "\n".join(
                [
                    "def shutdown_signal(*args):",
                    "    from PySide6 import QtCore",
                    "    QtCore.QCoreApplication.quit()",
                ]
            ),
        )
        source_text = source_text.replace(
            "\n".join(
                [
                    "def main_init(main_process_title = None):",
                    "    multiprocessing.freeze_support()",
                    "    multiprocessing.set_start_method('spawn')",
                    "    setproctitle.setproctitle(main_process_title)",
                    "    if main_is_frozen():",
                    "        cacert = os.path.join(os.path.dirname(sys.executable), 'botodata', 'cacert.pem')",
                    "        os.environ['AWS_CA_BUNDLE'] = cacert",
                    "        botodata = os.path.join(os.path.dirname(sys.executable), 'botodata')",
                    "        os.environ['AWS_DATA_PATH'] = botodata",
                    "    elif sys.platform == 'win32':",
                    "        myappid = 'com.sprocktech.' + main_process_title + '.' + __version__",
                    "        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)",
                    "    if not sys.stdout or sys.stderr:",
                    "        sys.stdout = open(os.devnull)",
                    "        sys.stderr = open(os.devnull)",
                    "    QtCore = QtCore",
                    "    import PySide6",
                    "    QtCore.QSettings.setDefaultFormat(QtCore.QSettings.Format.IniFormat)",
                    "    signal.signal(signal.SIGINT, shutdown_signal)",
                    "    signal.signal(signal.SIGTERM, shutdown_signal)",
                ]
            ),
            "\n".join(
                [
                    "def main_init(main_process_title = None):",
                    "    multiprocessing.freeze_support()",
                    "    try:",
                    "        multiprocessing.set_start_method('spawn')",
                    "    except RuntimeError:",
                    "        pass",
                    "    setproctitle.setproctitle(main_process_title)",
                    "    if main_is_frozen():",
                    "        cacert = os.path.join(os.path.dirname(sys.executable), 'botodata', 'cacert.pem')",
                    "        os.environ['AWS_CA_BUNDLE'] = cacert",
                    "        botodata = os.path.join(os.path.dirname(sys.executable), 'botodata')",
                    "        os.environ['AWS_DATA_PATH'] = botodata",
                    "    elif sys.platform == 'win32':",
                    "        myappid = 'com.sprocktech.' + main_process_title + '.' + __version__",
                    "        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)",
                    "    if not sys.stdout or not sys.stderr:",
                    "        sys.stdout = open(os.devnull)",
                    "        sys.stderr = open(os.devnull)",
                    "    from PySide6 import QtCore",
                    "    QtCore.QSettings.setDefaultFormat(QtCore.QSettings.Format.IniFormat)",
                    "    signal.signal(signal.SIGINT, shutdown_signal)",
                    "    signal.signal(signal.SIGTERM, shutdown_signal)",
                ]
            ),
        )
        source_text = source_text.replace(
            "\n".join(
                [
                    "if __name__ == '__main__':",
                    "    from gui import __main__",
                    "    __main__.main()",
                    "    return None",
                ]
            ),
            "\n".join(
                [
                    "if __name__ == '__main__':",
                    "    from .gui import __main__",
                    "    __main__.main()",
                ]
            ),
        )
    elif module_key == "acheron:hyperborea/__init__.py":
        source_text = source_text.replace(
            "\n".join(
                [
                    "try:",
                    "    from version import version as __version__",
                    "    return None",
                    "except ImportError:",
                    "    __version__ = 'UNKNOWN'",
                    "    return None",
                ]
            ),
            "\n".join(
                [
                    "try:",
                    "    from .version import version as __version__",
                    "except ImportError:",
                    "    try:",
                    "        from version import version as __version__",
                    "    except ImportError:",
                    "        __version__ = 'UNKNOWN'",
                ]
            ),
        )
    elif module_key == "mondo:mondo/__init__.py":
        source_text = source_text.replace("from export_script import matplotlib_wrapper as matplotlib", "from .export_script import matplotlib_wrapper as matplotlib")
        source_text = source_text.replace(
            "\n".join(
                [
                    "try:",
                    "    from version import version as __version__",
                    "except ImportError:",
                    "    __version__ = 'UNKNOWN'",
                ]
            ),
            "\n".join(
                [
                    "try:",
                    "    from .version import version as __version__",
                    "except ImportError:",
                    "    try:",
                    "        from version import version as __version__",
                    "    except ImportError:",
                    "        __version__ = 'UNKNOWN'",
                ]
            ),
        )
        source_text = re.sub(
            r"if __name__ == '__main__':\n\s+from\s+import __main__\n\s+__main__\.main\(\)\n\s+return None",
            "if __name__ == '__main__':\n    from . import __main__\n    __main__.main()",
            source_text,
        )
    elif module_key == "mondo:mondo/__main__.py":
        source_text = source_text.replace("import logging.handlers as logging", "import logging\nimport logging.handlers")
        source_text = source_text.replace("from main import MondoMainWindow", "from .main import MondoMainWindow")
        source_text = re.sub(r"if not sys\.stdout or sys\.stderr:", "if not sys.stdout or not sys.stderr:", source_text)
    return source_text


def is_class_code(code: types.CodeType) -> bool:
    if code.co_name.startswith("<"):
        return False
    if code.co_argcount or code.co_kwonlyargcount or code.co_posonlyargcount:
        return False
    instructions = [ins for ins in dis.get_instructions(code) if ins.opname not in {"MAKE_CELL", "COPY_FREE_VARS"}]
    if len(instructions) < 5:
        return False
    return (
        instructions[0].opname == "RESUME"
        and instructions[1].opname == "LOAD_NAME"
        and instructions[1].argval == "__name__"
        and instructions[2].opname == "STORE_NAME"
        and instructions[2].argval == "__module__"
        and instructions[3].opname == "LOAD_CONST"
        and instructions[4].opname == "STORE_NAME"
        and instructions[4].argval == "__qualname__"
    )


def symbol_expr(text: str) -> tuple[str, str]:
    return ("expr", text)


def symbol_const(value: object) -> tuple[str, object]:
    return ("const", value)


def symbol_code(code: types.CodeType) -> tuple[str, types.CodeType]:
    return ("code", code)


def as_expr(symbol: object) -> str | None:
    if isinstance(symbol, tuple) and symbol:
        if symbol[0] == "expr":
            return symbol[1]
        if symbol[0] == "const":
            return repr(symbol[1])
    return None


def as_const_string(symbol: object) -> str | None:
    if isinstance(symbol, tuple) and symbol and symbol[0] == "const" and isinstance(symbol[1], str):
        return symbol[1]
    return None


def format_call_expr(callable_expr: str, args: list[object], kw_names: tuple[str, ...] | None) -> str:
    rendered: list[str] = []
    if kw_names:
        positional_count = len(args) - len(kw_names)
        for item in args[:positional_count]:
            rendered.append(as_expr(item) or "...")
        for key, item in zip(kw_names, args[positional_count:]):
            rendered.append(f"{key}={as_expr(item) or '...'}")
    else:
        rendered.extend(as_expr(item) or "..." for item in args)
    if callable_expr == "dataclass" and not rendered:
        return "dataclass"
    return f"{callable_expr}({', '.join(rendered)})"


def load_name_expr(ins: dis.Instruction) -> str:
    if ins.opname == "LOAD_GLOBAL" and ins.argrepr:
        return ins.argrepr.split(" + ")[-1]
    return str(ins.argval)


def extract_module_class_metadata(module_code: types.CodeType) -> dict[str, ClassMetadata]:
    metadata: dict[str, ClassMetadata] = {}
    stack: list[object] = []
    kw_names: tuple[str, ...] | None = None
    pending_call_argc = 0

    for ins in dis.get_instructions(module_code):
        op = ins.opname
        if op in {"RESUME", "NOP", "CACHE", "POP_TOP", "COPY_FREE_VARS"}:
            continue
        if op == "PRECALL":
            pending_call_argc = int(ins.arg or 0)
            continue
        if op == "PUSH_NULL":
            continue
        if op in {"LOAD_NAME", "LOAD_GLOBAL"}:
            stack.append(symbol_expr(load_name_expr(ins)))
            continue
        if op == "LOAD_ATTR":
            target = stack.pop() if stack else None
            target_expr = as_expr(target)
            stack.append(symbol_expr(f"{target_expr}.{ins.argval}" if target_expr else str(ins.argval)))
            continue
        if op == "LOAD_CONST":
            value = ins.argval
            if isinstance(value, types.CodeType):
                stack.append(symbol_code(value))
            else:
                stack.append(symbol_const(value))
            continue
        if op == "LOAD_BUILD_CLASS":
            stack.append(symbol_expr("__build_class__"))
            continue
        if op == "MAKE_FUNCTION":
            code_symbol = stack.pop() if stack else None
            if isinstance(code_symbol, tuple) and code_symbol and code_symbol[0] == "code":
                stack.append(code_symbol)
            else:
                stack.append(symbol_expr("function"))
            continue
        if op == "KW_NAMES":
            value = module_code.co_consts[ins.arg]
            kw_names = tuple(value) if isinstance(value, tuple) else None
            continue
        if op == "CALL":
            argc = pending_call_argc
            pending_call_argc = 0
            if len(stack) < argc + 1:
                stack.clear()
                kw_names = None
                continue
            args = [stack.pop() for _ in range(argc)][::-1]
            callable_symbol = stack.pop() if stack else None
            callable_expr = as_expr(callable_symbol)
            if callable_expr == "__build_class__":
                code_symbol = args[0] if len(args) >= 1 else None
                name_symbol = args[1] if len(args) >= 2 else None
                class_name = as_const_string(name_symbol)
                if (
                    isinstance(code_symbol, tuple)
                    and code_symbol
                    and code_symbol[0] == "code"
                    and class_name
                ):
                    base_exprs = [as_expr(item) or "..." for item in args[2:]]
                    stack.append(ClassBuild(class_name, code_symbol[1], base_exprs, []))
                else:
                    stack.append(symbol_expr("build_class(...)"))
            elif callable_expr and len(args) == 1 and isinstance(args[0], ClassBuild):
                decorated = args[0]
                decorated.decorators.append(callable_expr)
                stack.append(decorated)
            elif callable_expr:
                stack.append(symbol_expr(format_call_expr(callable_expr, args, kw_names)))
            else:
                stack.append(symbol_expr("call(...)"))
            kw_names = None
            continue
        if op == "STORE_NAME":
            value = stack.pop() if stack else None
            if isinstance(value, ClassBuild):
                metadata[ins.argval] = ClassMetadata(
                    name=value.name,
                    bases=value.bases,
                    decorators=value.decorators,
                )
            continue
        stack.clear()
        kw_names = None
        pending_call_argc = 0

    return metadata


def render_class_statements(code: types.CodeType, indent: str) -> list[str]:
    method_names = {child.co_name for child in iter_child_codes(code)}
    lines: list[str] = []
    stack: list[object] = []
    kw_names: tuple[str, ...] | None = None
    pending_call_argc = 0

    for ins in dis.get_instructions(code):
        op = ins.opname
        if op in {"RESUME", "NOP", "CACHE", "SETUP_ANNOTATIONS", "MAKE_CELL", "COPY_FREE_VARS"}:
            continue
        if op == "PRECALL":
            pending_call_argc = int(ins.arg or 0)
            continue
        if op == "PUSH_NULL":
            continue
        if op in {"LOAD_NAME", "LOAD_GLOBAL", "LOAD_DEREF"}:
            stack.append(symbol_expr(load_name_expr(ins)))
            continue
        if op == "LOAD_CONST":
            value = ins.argval
            if isinstance(value, types.CodeType):
                stack.append(symbol_code(value))
            else:
                stack.append(symbol_const(value))
            continue
        if op == "LOAD_ATTR":
            target = stack.pop() if stack else None
            target_expr = as_expr(target)
            stack.append(symbol_expr(f"{target_expr}.{ins.argval}" if target_expr else str(ins.argval)))
            continue
        if op == "MAKE_FUNCTION":
            code_symbol = stack.pop() if stack else None
            if isinstance(code_symbol, tuple) and code_symbol and code_symbol[0] == "code":
                stack.append(code_symbol)
            else:
                stack.append(symbol_expr("function"))
            continue
        if op == "KW_NAMES":
            value = code.co_consts[ins.arg]
            kw_names = tuple(value) if isinstance(value, tuple) else None
            continue
        if op == "CALL":
            argc = pending_call_argc
            pending_call_argc = 0
            if len(stack) < argc + 1:
                stack.clear()
                kw_names = None
                continue
            args = [stack.pop() for _ in range(argc)][::-1]
            callable_symbol = stack.pop() if stack else None
            callable_expr = as_expr(callable_symbol)
            if callable_expr:
                stack.append(symbol_expr(format_call_expr(callable_expr, args, kw_names)))
            else:
                stack.append(symbol_expr("call(...)"))
            kw_names = None
            continue
        if op == "STORE_SUBSCR":
            if len(stack) < 3:
                stack.clear()
                kw_names = None
                pending_call_argc = 0
                continue
            key_symbol = stack.pop() if stack else None
            container_symbol = stack.pop() if stack else None
            value_symbol = stack.pop() if stack else None
            if as_expr(container_symbol) == "__annotations__":
                key = as_const_string(key_symbol)
                value_expr = as_expr(value_symbol)
                if key and value_expr:
                    lines.append(f"{indent}    {key}: {value_expr}")
            continue
        if op == "STORE_NAME":
            name = str(ins.argval)
            value_symbol = stack.pop() if stack else None
            if name in {"__module__", "__qualname__", "__classcell__"}:
                continue
            if name in method_names:
                continue
            if isinstance(value_symbol, tuple) and value_symbol and value_symbol[0] == "code":
                continue
            value_expr = as_expr(value_symbol)
            if value_expr:
                lines.append(f"{indent}    {name} = {value_expr}")
            continue
        if op in {"RETURN_VALUE", "POP_TOP"}:
            continue
        stack.clear()
        kw_names = None
        pending_call_argc = 0

    deduped: list[str] = []
    seen: set[str] = set()
    for line in lines:
        if line in seen:
            continue
        seen.add(line)
        deduped.append(line)
    return deduped


def build_signature(code: types.CodeType) -> str:
    params: list[str] = []
    varnames = list(code.co_varnames)
    index = 0

    posonly_count = code.co_posonlyargcount
    positional_count = code.co_argcount - posonly_count

    for _ in range(posonly_count):
        params.append(varnames[index])
        index += 1
    if posonly_count:
        params.append("/")

    for _ in range(positional_count):
        params.append(varnames[index])
        index += 1

    has_varargs = bool(code.co_flags & inspect.CO_VARARGS)
    has_varkw = bool(code.co_flags & inspect.CO_VARKEYWORDS)

    if has_varargs:
        params.append(f"*{varnames[index]}")
        index += 1
    elif code.co_kwonlyargcount:
        params.append("*")

    for _ in range(code.co_kwonlyargcount):
        params.append(varnames[index])
        index += 1

    if has_varkw:
        params.append(f"**{varnames[index]}")

    return ", ".join(params)


def load_snippet_body(snippet_dir: Path, qualname: str) -> str | None:
    path = snippet_dir / f"{sanitize_qualname(qualname)}.py"
    if not path.exists():
        return None

    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    while lines and (lines[0].startswith("# Source Generated") or lines[0].startswith("# File:")):
        lines.pop(0)
    while lines and not lines[0].strip():
        lines.pop(0)

    filtered = [line for line in lines if not line.startswith("# WARNING:")]
    while filtered and not filtered[0].strip():
        filtered.pop(0)
    while filtered and not filtered[-1].strip():
        filtered.pop()

    if not filtered:
        return None
    return "\n".join(filtered)


def indent_block(text: str, indent: str) -> str:
    return "\n".join(f"{indent}{line}" if line else indent.rstrip() for line in text.splitlines())


def snippet_is_syntax_valid(prefix: str, signature: str, body: str) -> bool:
    sample = f"{prefix} __snippet__({signature}):\n{indent_block(body, '    ')}\n"
    try:
        compile(sample, "<assembled-snippet>", "exec")
    except SyntaxError:
        return False
    return not bool(SUSPICIOUS_SNIPPET_RE.search(body))


def render_disassembly_fallback(code: types.CodeType, indent: str) -> str:
    lines = [
        f"{indent}# TODO: pycdc could not reconstruct this body.",
        f"{indent}# Signature was recovered from the code object; default values may need manual repair.",
        f"{indent}# Bytecode excerpt:",
    ]
    for index, instruction in enumerate(dis.get_instructions(code)):
        if index >= MAX_DISASSEMBLY_LINES:
            lines.append(f"{indent}# ... bytecode truncated ...")
            break
        arg_part = f" {instruction.argrepr}" if instruction.argrepr else ""
        lines.append(f"{indent}# {instruction.offset:>4} {instruction.opname}{arg_part}")
    lines.append(f"{indent}pass")
    return "\n".join(lines)


def render_function(
    code: types.CodeType,
    module_key: str,
    snippet_dir: Path,
    indent: str,
    stats: AssemblyStats,
) -> str:
    prefix = "async def" if code.co_flags & (inspect.CO_COROUTINE | inspect.CO_ASYNC_GENERATOR) else "def"
    signature = MANUAL_SIGNATURE_OVERRIDES.get((module_key, code.co_qualname), build_signature(code))
    header = f"{indent}{prefix} {code.co_name}({signature}):"

    body = MANUAL_FUNCTION_OVERRIDES.get((module_key, code.co_qualname))
    if body is None:
        body = load_snippet_body(snippet_dir, code.co_qualname)

    if body is None or not snippet_is_syntax_valid(prefix, signature, body):
        stats.fallback_functions += 1
        rendered_body = render_disassembly_fallback(code, indent + "    ")
    else:
        stats.snippet_functions += 1
        rendered_body = indent_block(body, indent + "    ")

    return f"{header}\n{rendered_body}"


def render_class(
    code: types.CodeType,
    module_key: str,
    class_bases: dict[str, str],
    module_class_metadata: dict[str, ClassMetadata],
    snippet_dir: Path,
    indent: str,
    stats: AssemblyStats,
) -> str:
    metadata = module_class_metadata.get(code.co_name)
    bases = metadata.bases if metadata and metadata.bases else None
    if bases is None:
        parsed_bases = class_bases.get(code.co_name, "")
        bases = [parsed_bases] if parsed_bases else []

    decorators = metadata.decorators if metadata else []

    members: list[str] = []
    statement_lines = render_class_statements(code, indent)
    members.extend(statement_lines)

    child_codes = [child for child in iter_child_codes(code) if not child.co_name.startswith("<")]
    child_method_names = [child.co_name for child in child_codes if not is_class_code(child)]

    if not bases:
        if any("= enum.auto()" in line for line in statement_lines):
            bases = ["enum.Enum"]
        elif (
            not child_method_names
            and statement_lines
            and all(": " in line and "=" not in line for line in statement_lines)
        ):
            decorators = decorators or ["dataclass"]

    decorator_lines = [f"{indent}@{decorator}" for decorator in decorators]
    suffix = f"({', '.join(bases)})" if bases else ""
    header = f"{indent}class {code.co_name}{suffix}:"

    for child in child_codes:
        if child.co_name.startswith("<"):
            continue
        if is_class_code(child):
            members.append(render_class(child, module_key, class_bases, {}, snippet_dir, indent + "    ", stats))
        else:
            members.append(render_function(child, module_key, snippet_dir, indent + "    ", stats))

    if not members:
        members.append(f"{indent}    pass")

    lines = decorator_lines + [header, "", "\n\n".join(members)]
    return "\n".join(lines)


def assemble_module(package: str, pyc_path: Path) -> AssemblyStats:
    rel = pyc_path.relative_to(PYC_ROOT / package)
    source_path = SRC_ROOT / package / rel.with_suffix(".py")
    assembled_path = ASSEMBLED_SRC_ROOT / package / rel.with_suffix(".py")
    snippet_dir = SNIPPET_ROOT / package / rel.with_suffix("")
    module_key = f"{package}:{rel.with_suffix('.py').as_posix()}"

    source_text = source_path.read_text(encoding="utf-8", errors="ignore")
    source_text = apply_module_text_replacements(module_key, source_text)
    assembled_path.parent.mkdir(parents=True, exist_ok=True)

    stats = AssemblyStats(
        package=package,
        pyc_path=str(pyc_path.relative_to(ROOT)),
        source_path=str(source_path.relative_to(ROOT)),
        assembled_path=str(assembled_path.relative_to(ROOT)),
        mode="copied_clean",
        top_level_items=0,
        snippet_functions=0,
        fallback_functions=0,
    )

    if (
        module_key not in FORCE_RECONSTRUCT_MODULES
        and "# WARNING: Decompyle incomplete" not in source_text
        and source_text_is_trustworthy(source_text)
    ):
        assembled_path.write_text(source_text, encoding="utf-8")
        return stats

    code = load_code(pyc_path)
    children = [child for child in iter_child_codes(code) if not child.co_name.startswith("<")]
    stats.mode = "reconstructed"
    stats.top_level_items = len(children)

    blocks: list[str] = []
    preamble = extract_preamble(source_text)
    if preamble:
        blocks.append(sanitize_preamble(preamble, source_path))

    blocks.append(
        "\n".join(
            [
                "# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.",
                "# NOTE: function defaults and some class-level assignments may need manual repair.",
            ]
        )
    )

    class_bases = parse_class_bases(source_text)
    module_class_metadata = extract_module_class_metadata(code)
    rendered_items: list[str] = []
    for child in children:
        if is_class_code(child):
            rendered_items.append(render_class(child, module_key, class_bases, module_class_metadata, snippet_dir, "", stats))
        else:
            rendered_items.append(render_function(child, module_key, snippet_dir, "", stats))

    if rendered_items:
        blocks.append("\n\n".join(rendered_items))

    assembled_path.write_text("\n\n".join(blocks).rstrip() + "\n", encoding="utf-8")
    return stats


def write_readme(results: list[AssemblyStats]) -> None:
    copied = sum(1 for item in results if item.mode == "copied_clean")
    reconstructed = sum(1 for item in results if item.mode == "reconstructed")
    snippet_functions = sum(item.snippet_functions for item in results)
    fallback_functions = sum(item.fallback_functions for item in results)
    text = f"""# Assembled Python Sources

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

- modules copied clean: {copied}
- modules reconstructed: {reconstructed}
- functions recovered from snippets: {snippet_functions}
- functions using disassembly fallback: {fallback_functions}

## Regeneration

```bash
python3.11 tools/assemble_recovered_sources.py
```
"""
    ASSEMBLED_README.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Assemble editable Python files from recovered decompilation artifacts.")
    parser.add_argument(
        "--packages",
        nargs="+",
        choices=["acheron", "mondo"],
        default=["acheron", "mondo"],
        help="Packages to assemble.",
    )
    args = parser.parse_args()

    ensure_clean_dir(ASSEMBLED_SRC_ROOT)

    results: list[AssemblyStats] = []
    for package in args.packages:
        package_root = PYC_ROOT / package
        for pyc_path in sorted(package_root.rglob("*.pyc")):
            results.append(assemble_module(package, pyc_path))

    ASSEMBLED_ROOT.mkdir(parents=True, exist_ok=True)
    ASSEMBLED_MANIFEST.write_text(
        json.dumps([asdict(item) for item in results], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    write_readme(results)

    copied = sum(1 for item in results if item.mode == "copied_clean")
    reconstructed = sum(1 for item in results if item.mode == "reconstructed")
    print(
        f"assembled_modules={len(results)} copied_clean={copied} reconstructed={reconstructed} "
        f"manifest={ASSEMBLED_MANIFEST}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
