# Source Generated with Decompyle++
# File: tmp9zniz_2y.marshal (Python 3.11)

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
from  import mondo_rc
logger = logging.getLogger(__name__)
ignored_types = builtins.__dict__.values()()
ignored_types.remove(list)
ignored_types.append(type(None))

def is_ignored_type(value):
    if isinstance(value, QtCore.QObject):
        return True
    for t in None:
        if type(value) == t:
            return True
        return False


class CommandList(list):
    
    def __init__(self, setup_commands = (None,)):
        self.plotdata = { }
        self._index = 0
        if not setup_commands:
            self.append('import matplotlib')
            self.append('import numpy')
            self.append('from PySide6 import QtGui')
            self.append('')
            return None
        None.extend(setup_commands)
        self.append('')
        self.append("plotdata = numpy.load(__file__ + '.npz')")

    
    def get_string(self, value):
        if isinstance(value, numpy.ndarray):
            i = 'array_{}'.format(self._index)
            value = self, self._index += 1, ._index
            return "plotdata['{}']".format(i)
        return None(value)

    
    def output(self, scriptfile):
        datafile = scriptfile + '.npz'
        logger.debug('Writing script to {}'.format(scriptfile))
        f = open(scriptfile, 'wt', encoding = 'utf_8')
        for v in self:
            s = str(v)
            if s == 'fig.show()':
                s = 'plt.show()'
            f.write(s)
            f.write('\n')
            None(None, None)
        with None:
            if not None:
                pass
        logger.debug('Writing script data to {}'.format(datafile))
    # WARNING: Decompyle incomplete



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
        pass
    # WARNING: Decompyle incomplete



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
    
    def __init__(self = None, wrapped = None, name = None, cmd_list = ('cmd_list', CommandList)):
        self._wrapped = wrapped
        self._name = name
        self._cmd_list = cmd_list

    
    def __getattribute__(self, attr):
        pass
    # WARNING: Decompyle incomplete

    
    def __getitem__(self, key):
        wrapped = object.__getattribute__(self, '_wrapped')
        name = object.__getattribute__(self, '_name')
        cmd_list = object.__getattribute__(self, '_cmd_list')
        new_name = GetItemCommand(cmd_list, name, key)
        value = wrapped.__getitem__(key)
        if is_ignored_type(value):
            return value
        return None(value, new_name, cmd_list)

    
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



def get_script_file(default_name = None, parent = None):
    settings = QtCore.QSettings()
    directory = settings.value('fileSaveDirectory')
    if directory and isinstance(directory, str):
        if not os.path.isdir(directory):
            directory = None
        else:
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


def add_export_script_action(figure = None, cmd_list = None):
    pass
# WARNING: Decompyle incomplete

subplots_wrapper = (lambda nrows = None, ncols = None, *, squeeze, sharex: pass)()
subplots_wrapper = (lambda nrows = None, ncols = None, *, sharex, sharey: pass)()

def subplots_wrapper(*args, **kwargs):
    pass
# WARNING: Decompyle incomplete

setup_commands = CommandList()
matplotlib_wrapper: ModuleType = Wrapper(matplotlib, 'matplotlib', setup_commands)
