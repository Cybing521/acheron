# Source Generated with Decompyle++
# File: export_script.pyc (Python 3.11)

import builtins
import gc
import logging
import os.path as os
from types import ModuleType
from typing import Any, Literal, Optional, overload
import matplotlib.figure as matplotlib
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy
from PySide6 import QtCore, QtGui, QtWidgets
import matplotlib
from . import mondo_rc
logger = logging.getLogger(__name__)
ignored_types = list(builtins.__dict__.values())
ignored_types.remove(list)
ignored_types.append(type(None))

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

def is_ignored_type(value):
    if isinstance(value, QtCore.QObject):
        return True
    for t in ignored_types:
        if type(value) == t:
            return True
    return False

class CommandList(list):

    def __init__(self, setup_commands):
        self.plotdata = {}
        self._index = 0
        if not setup_commands:
            self.append('import matplotlib')
            self.append('import numpy')
            self.append('from PySide6 import QtGui')
            self.append('')
            return None
        self.extend(setup_commands)
        self.append('')
        self.append("plotdata = numpy.load(__file__ + '.npz')")
        return None

    def get_string(self, value):
        if isinstance(value, numpy.ndarray):
            i = 'array_{}'.format(self._index)
            self._index += 1
            self.plotdata[i] = value
            return "plotdata['{}']".format(i)
        return repr(value)

    def output(self, scriptfile):
        datafile = scriptfile + '.npz'
        logger.debug('Writing script to {}'.format(scriptfile))
        with open(scriptfile, 'wt', encoding='utf_8') as f:
            for v in self:
                s = str(v)
                if s == 'fig.show()':
                    s = 'plt.show()'
                f.write(s)
                f.write('\n')
        logger.debug('Writing script data to {}'.format(datafile))
        if self.plotdata:
            numpy.savez(datafile, **self.plotdata)
        return None

class AttributeCommand:

    def __init__(self, cmd_list, base, attr):
        self.cmd_list = cmd_list
        self.base = base
        self.attr = attr

    def __repr__(self):
        return '{}.{}'.format(self.base, self.attr)

class CallCommand:

    def __init__(self, cmd_list, base, func, *args, **kwargs):
        self.cmd_list = cmd_list
        self.base = base
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def __repr__(self):
        params = [self.cmd_list.get_string(value) for value in self.args]
        for key, value in self.kwargs.items():
            params.append(f'{key}={self.cmd_list.get_string(value)}')
        param_str = ', '.join(params)
        return '{}.{}({})'.format(self.base, self.func, param_str)

class GetItemCommand:

    def __init__(self, cmd_list, base, key):
        self.cmd_list = cmd_list
        self.base = base
        self.key = key

    def __repr__(self):
        return '{}[{}]'.format(self.base, self.cmd_list.get_string(self.key))

class SetItemCommand:

    def __init__(self, cmd_list, base, key, value):
        self.cmd_list = cmd_list
        self.base = base
        self.key = key
        self.value = value

    def __repr__(self):
        return '{}[{}] = {}'.format(self.base, self.cmd_list.get_string(self.key), self.cmd_list.get_string(self.value))

class Wrapper:

    def __init__(self, wrapped, name, cmd_list):
        self._wrapped = wrapped
        self._name = name
        self._cmd_list = cmd_list

    def __getattribute__(self, attr):
        wrapped = object.__getattribute__(self, '_wrapped')
        name = object.__getattribute__(self, '_name')
        cmd_list = object.__getattribute__(self, '_cmd_list')
        orig_attr = wrapped.__getattribute__(attr)
        if callable(orig_attr):
            def wrapped_func(*args, **kwargs):
                new_name = AttributeCommand(cmd_list, name, attr)
                result = orig_attr(*args, **kwargs)
                cmd_list.append(CallCommand(cmd_list, name, attr, *args, **kwargs))
                if is_ignored_type(result):
                    return result
                return Wrapper(result, new_name, cmd_list)

            return wrapped_func
        if is_ignored_type(orig_attr):
            return orig_attr
        new_name = AttributeCommand(cmd_list, name, attr)
        return Wrapper(orig_attr, new_name, cmd_list)

    def __getitem__(self, key):
        wrapped = object.__getattribute__(self, '_wrapped')
        name = object.__getattribute__(self, '_name')
        cmd_list = object.__getattribute__(self, '_cmd_list')
        new_name = GetItemCommand(cmd_list, name, key)
        value = wrapped.__getitem__(key)
        if is_ignored_type(value):
            return value
        return Wrapper(value, new_name, cmd_list)

    def __setitem__(self, key, value):
        wrapped = object.__getattribute__(self, '_wrapped')
        name = object.__getattribute__(self, '_name')
        cmd_list = object.__getattribute__(self, '_cmd_list')
        cmd_list.append(SetItemCommand(cmd_list, name, key, value))
        return wrapped.__setitem__(key, value)

    def __len__(self):
        wrapped = object.__getattribute__(self, '_wrapped')
        return wrapped.__len__()

    def __iter__(self):
        wrapped = object.__getattribute__(self, '_wrapped')
        return wrapped.__iter__()

def get_script_file(default_name, parent):
    settings = QtCore.QSettings()
    directory = settings.value('fileSaveDirectory')
    if directory and isinstance(directory, str):
        if not os.path.isdir(directory):
            directory = None
    if not directory:
        directory = ''
    file_and_dir = os.path.join(directory, default_name)
    caption = 'Save File'
    file_filter = 'Python Script (*.py);;All Files (*.*)'
    val = QtWidgets.QFileDialog.getSaveFileName(parent, caption, file_and_dir, file_filter)
    output_path = val[0]
    if output_path:
        output_dir = os.path.dirname(output_path)
        settings.setValue('fileSaveDirectory', output_dir)
        return output_path

def add_export_script_action(figure, cmd_list):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 MAKE_CELL cmd_list
    #    2 MAKE_CELL toolbar
    #    4 RESUME
    #    6 LOAD_FAST figure
    #    8 LOAD_ATTR canvas
    #   18 LOAD_ATTR toolbar
    #   28 STORE_DEREF toolbar
    #   30 LOAD_GLOBAL QtWidgets
    #   42 LOAD_ATTR QApplication
    #   52 LOAD_METHOD translate
    #   74 LOAD_CONST 'ExportScript'
    #   76 LOAD_CONST 'Export Script'
    #   78 PRECALL
    #   82 CALL
    #   92 STORE_FAST actionText
    #   94 LOAD_GLOBAL NULL + QtGui
    #  106 LOAD_ATTR QAction
    #  116 LOAD_FAST actionText
    #  118 LOAD_DEREF toolbar
    #  120 PRECALL
    #  124 CALL
    #  134 STORE_FAST action
    #  136 LOAD_FAST action
    #  138 LOAD_METHOD setIcon
    #  160 LOAD_GLOBAL QtGui
    #  172 LOAD_ATTR QIcon
    #  182 LOAD_METHOD fromTheme
    #  204 LOAD_CONST 'scroll'
    #  206 PRECALL
    #  210 CALL
    #  220 PRECALL
    #  224 CALL
    #  234 POP_TOP
    #  236 LOAD_CLOSURE cmd_list
    #  238 LOAD_CLOSURE toolbar
    #  240 BUILD_TUPLE
    #  242 LOAD_CONST <code object handle_export at 0x105a73ab0, file "mondo\export_script.py", line 258>
    #  244 MAKE_FUNCTION closure
    #  246 STORE_FAST handle_export
    #  248 LOAD_FAST action
    #  250 LOAD_ATTR triggered
    #  260 LOAD_METHOD connect
    #  282 LOAD_FAST handle_export
    #  284 PRECALL
    #  288 CALL
    #  298 POP_TOP
    #  300 LOAD_DEREF toolbar
    #  302 LOAD_METHOD addAction
    #  324 LOAD_FAST action
    #  326 PRECALL
    #  330 CALL
    #  340 POP_TOP
    #  342 LOAD_CONST None
    #  344 RETURN_VALUE
    pass

def subplots_wrapper(*args, **kwargs):
    import matplotlib.pyplot as plt

    cmd_list = CommandList(setup_commands)
    cmd_list.append('')
    cmd_list.append('import matplotlib.pyplot as plt')
    cmd_list.append('')
    fig, ax = plt.subplots(*args, **kwargs)

    def handle_close(_event):
        gc.collect()

    fig.canvas.mpl_connect('close_event', handle_close)
    fig._export_script_commands = cmd_list
    add_export_script_action(fig, cmd_list)
    return (fig, ax)


setup_commands: list[str] = []
matplotlib_wrapper = matplotlib
matplotlib_wrapper.subplots = subplots_wrapper
