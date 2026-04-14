# Source Generated with Decompyle++
# File: unit_preferences.pyc (Python 3.11)

from dataclasses import dataclass
import math
from typing import Optional, TypedDict
from PySide6 import QtCore, QtWidgets
import asphodel
from .preferences import read_bool_setting, write_bool_setting
from .ui.ui_unit_preferences_widget import Ui_UnitPreferencesWidget

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

class UnitType(TypedDict):

    unit_type: int

    setting_name: str

    scale: float

    offset: float

class UnitButtonType(TypedDict):

    group: QtWidgets.QButtonGroup

    metric: QtWidgets.QRadioButton

    us: QtWidgets.QRadioButton

@dataclass
class UnitOption:

    unit_formatter: asphodel.AsphodelNativeUnitFormatter

    metric: bool

    non_metric: bool

    base_str: str

def get_unit_options(unit_type, minimum, maximum, resolution):
    metric_formatter = asphodel.nativelib.create_unit_formatter(unit_type, minimum, maximum, resolution, use_metric = True)
    us_formatter = asphodel.nativelib.create_unit_formatter(unit_type, minimum, maximum, resolution, use_metric = False)
    metric_scale = None
    base_str = metric_formatter.unit_utf8
    if metric_formatter.conversion_offset == 0:
        uf_1000x = asphodel.nativelib.create_unit_formatter(unit_type, minimum * 1000, maximum * 1000, resolution, use_metric = True)
        ratio = metric_formatter.conversion_scale / uf_1000x.conversion_scale
        if math.isclose(1000, ratio):
            metric_scale = 1 / metric_formatter.conversion_scale
            uf_base = asphodel.nativelib.create_unit_formatter(unit_type, 1, 1, 1, use_metric = True)
            base_str = uf_base.unit_utf8
    unit_options = [
        UnitOption(unit_formatter = metric_formatter, metric = True, non_metric = metric_formatter == us_formatter, alt_setting_name = None, base_str = base_str, metric_scale = metric_scale, metric_relation = None)]
    if metric_formatter != us_formatter:
        metric_relation = asphodel.nativelib.format_value_utf8(unit_type, 0, 1 / us_formatter.conversion_scale, use_metric = True)
        unit_options.append(UnitOption(unit_formatter = us_formatter, metric = False, non_metric = True, alt_setting_name = None, base_str = us_formatter.unit_utf8, metric_scale = None, metric_relation = metric_relation))

def get_default_option(settings, unit_type, unit_options):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 LOAD_GLOBAL NULL + read_bool_setting
    #   14 LOAD_FAST settings
    #   16 LOAD_CONST 'UseMixed'
    #   18 LOAD_CONST False
    #   20 PRECALL
    #   24 CALL
    #   34 STORE_FAST use_mixed
    #   36 LOAD_FAST use_mixed
    #   38 POP_JUMP_FORWARD_IF_FALSE to 222
    #   40 LOAD_FAST unit_options
    #   42 GET_ITER
    #   44 FOR_ITER to 110
    #   46 STORE_FAST unit_option
    #   48 LOAD_FAST unit_option
    #   50 LOAD_ATTR alt_setting_name
    #   60 STORE_FAST setting_name
    #   62 LOAD_FAST setting_name
    #   64 POP_JUMP_FORWARD_IF_FALSE to 108
    #   66 LOAD_GLOBAL NULL + read_bool_setting
    #   78 LOAD_FAST settings
    #   80 LOAD_FAST setting_name
    #   82 LOAD_CONST False
    #   84 PRECALL
    #   88 CALL
    #   98 POP_JUMP_FORWARD_IF_FALSE to 108
    #  100 LOAD_FAST unit_option
    #  102 SWAP
    #  104 POP_TOP
    #  106 RETURN_VALUE
    #  108 JUMP_BACKWARD to 44
    #  110 LOAD_GLOBAL NULL + read_bool_setting
    #  122 LOAD_FAST settings
    #  124 LOAD_CONST 'UseMetric'
    #  126 LOAD_CONST True
    #  128 PRECALL
    #  132 CALL
    #  142 STORE_FAST use_metric_overall
    #  144 LOAD_CONST 'UseMetricType{}'
    #  146 LOAD_METHOD format
    #  168 LOAD_FAST unit_type
    #  170 PRECALL
    #  174 CALL
    #  184 STORE_FAST setting_name
    #  186 LOAD_GLOBAL NULL + read_bool_setting
    #  198 LOAD_FAST settings
    #  200 LOAD_FAST setting_name
    #  202 LOAD_FAST use_metric_overall
    #  204 PRECALL
    #  208 CALL
    #  218 STORE_FAST use_metric
    #  220 JUMP_FORWARD to 256
    #  222 LOAD_GLOBAL NULL + read_bool_setting
    #  234 LOAD_FAST settings
    #  236 LOAD_CONST 'UseMetric'
    #  238 LOAD_CONST True
    #  240 PRECALL
    #  244 CALL
    #  254 STORE_FAST use_metric
    #  256 LOAD_FAST unit_options
    #  258 GET_ITER
    #  260 FOR_ITER to 316
    #  262 STORE_FAST unit_option
    #  264 LOAD_FAST use_metric
    #  266 POP_JUMP_FORWARD_IF_FALSE to 292
    #  268 LOAD_FAST unit_option
    #  270 LOAD_ATTR metric
    #  280 POP_JUMP_FORWARD_IF_FALSE to 290
    #  282 LOAD_FAST unit_option
    #  284 SWAP
    #  286 POP_TOP
    #  288 RETURN_VALUE
    #  290 JUMP_BACKWARD to 260
    #  292 LOAD_FAST unit_option
    #  294 LOAD_ATTR non_metric
    #  304 POP_JUMP_FORWARD_IF_FALSE to 314
    #  306 LOAD_FAST unit_option
    #  308 SWAP
    #  310 POP_TOP
    #  312 RETURN_VALUE
    # ... bytecode truncated ...
    pass

def create_unit_formatter(settings, unit_type, minimum, maximum, resolution):
    unit_options = get_unit_options(unit_type, minimum, maximum, resolution)
    option = get_default_option(settings, unit_type, unit_options)
    return option.unit_formatter

class UnitPreferencesWidget(Ui_UnitPreferencesWidget, QtWidgets.QWidget):

    def __init__(self, parent):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 COPY_FREE_VARS
        #    2 RESUME
        #    4 LOAD_GLOBAL NULL + super
        #   16 PRECALL
        #   20 CALL
        #   30 LOAD_METHOD __init__
        #   52 LOAD_FAST parent
        #   54 PRECALL
        #   58 CALL
        #   68 POP_TOP
        #   70 LOAD_GLOBAL NULL + QtCore
        #   82 LOAD_ATTR QSettings
        #   92 PRECALL
        #   96 CALL
        #  106 LOAD_FAST self
        #  108 STORE_ATTR settings
        #  118 BUILD_MAP
        #  120 LOAD_FAST self
        #  122 STORE_ATTR unit_buttons
        #  132 LOAD_FAST self
        #  134 LOAD_METHOD setupUi
        #  156 LOAD_FAST self
        #  158 PRECALL
        #  162 CALL
        #  172 POP_TOP
        #  174 LOAD_FAST self
        #  176 LOAD_METHOD _create_unit_buttons
        #  198 PRECALL
        #  202 CALL
        #  212 POP_TOP
        #  214 LOAD_FAST self
        #  216 LOAD_ATTR metricUnits
        #  226 LOAD_ATTR toggled
        #  236 LOAD_METHOD connect
        #  258 LOAD_FAST self
        #  260 LOAD_ATTR toggled_metric
        #  270 PRECALL
        #  274 CALL
        #  284 POP_TOP
        #  286 LOAD_FAST self
        #  288 LOAD_ATTR usUnits
        #  298 LOAD_ATTR toggled
        #  308 LOAD_METHOD connect
        #  330 LOAD_FAST self
        #  332 LOAD_ATTR toggled_us
        #  342 PRECALL
        #  346 CALL
        #  356 POP_TOP
        #  358 LOAD_FAST self
        #  360 LOAD_ATTR mixedUnits
        #  370 LOAD_ATTR toggled
        #  380 LOAD_METHOD connect
        #  402 LOAD_FAST self
        #  404 LOAD_ATTR toggled_mixed
        #  414 PRECALL
        #  418 CALL
        #  428 POP_TOP
        #  430 LOAD_FAST self
        #  432 LOAD_ATTR unitGridLayout
        #  442 LOAD_METHOD setColumnStretch
        #  464 LOAD_CONST 0
        #  466 LOAD_CONST 1
        #  468 PRECALL
        #  472 CALL
        #  482 POP_TOP
        #  484 LOAD_FAST self
        #  486 LOAD_ATTR unitGridLayout
        #  496 LOAD_METHOD setColumnStretch
        #  518 LOAD_CONST 1
        #  520 LOAD_CONST 1
        #  522 PRECALL
        #  526 CALL
        #  536 POP_TOP
        #  538 LOAD_FAST self
        #  540 LOAD_ATTR unitGridLayout
        #  550 LOAD_METHOD setColumnStretch
        #  572 LOAD_CONST 2
        #  574 LOAD_CONST 1
        #  576 PRECALL
        #  580 CALL
        # ... bytecode truncated ...
        pass

    def _create_unit_buttons(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_GLOBAL asphodel
        #   14 LOAD_ATTR unit_type_names
        #   24 GET_ITER
        #   26 EXTENDED_ARG
        #   28 FOR_ITER to 1560
        #   30 STORE_FAST unit_type_name
        #   32 LOAD_GLOBAL NULL + getattr
        #   44 LOAD_GLOBAL asphodel
        #   56 LOAD_FAST unit_type_name
        #   58 PRECALL
        #   62 CALL
        #   72 STORE_FAST unit_type
        #   74 LOAD_GLOBAL asphodel
        #   86 LOAD_ATTR nativelib
        #   96 LOAD_METHOD create_unit_formatter
        #  118 LOAD_FAST unit_type
        #  120 LOAD_CONST 0.0
        #  122 LOAD_CONST 0.0
        #  124 LOAD_CONST 0.0
        #  126 LOAD_CONST True
        #  128 KW_NAMES
        #  130 PRECALL
        #  134 CALL
        #  144 STORE_FAST metric_formatter
        #  146 LOAD_GLOBAL asphodel
        #  158 LOAD_ATTR nativelib
        #  168 LOAD_METHOD create_unit_formatter
        #  190 LOAD_FAST unit_type
        #  192 LOAD_CONST 0.0
        #  194 LOAD_CONST 0.0
        #  196 LOAD_CONST 0.0
        #  198 LOAD_CONST False
        #  200 KW_NAMES
        #  202 PRECALL
        #  206 CALL
        #  216 STORE_FAST us_formatter
        #  218 LOAD_CONST None
        #  220 STORE_FAST alt_button
        #  222 LOAD_CONST None
        #  224 STORE_FAST alt_setting
        #  226 LOAD_GLOBAL alternate_units
        #  238 GET_ITER
        #  240 FOR_ITER to 504
        #  242 STORE_FAST alternate_unit
        #  244 LOAD_FAST unit_type
        #  246 LOAD_FAST alternate_unit
        #  248 LOAD_CONST 'unit_type'
        #  250 BINARY_SUBSCR
        #  260 COMPARE_OP ==
        #  266 POP_JUMP_FORWARD_IF_FALSE to 502
        #  268 LOAD_FAST alternate_unit
        #  270 LOAD_CONST 'setting_name'
        #  272 BINARY_SUBSCR
        #  282 STORE_FAST alt_setting
        #  284 LOAD_GLOBAL NULL + QtWidgets
        #  296 LOAD_ATTR QRadioButton
        #  306 LOAD_FAST self
        #  308 PRECALL
        #  312 CALL
        #  322 STORE_FAST alt_button
        #  324 LOAD_FAST alternate_unit
        #  326 LOAD_CONST 'unit_strings'
        #  328 BINARY_SUBSCR
        #  338 LOAD_CONST 1
        #  340 BINARY_SUBSCR
        #  350 STORE_FAST alt_name
        #  352 LOAD_FAST metric_formatter
        #  354 LOAD_METHOD format_utf8
        #  376 LOAD_CONST 1
        #  378 LOAD_FAST alternate_unit
        #  380 LOAD_CONST 'scale'
        #  382 BINARY_SUBSCR
        #  392 BINARY_OP /
        #  396 PRECALL
        #  400 CALL
        #  410 STORE_FAST metric_relation
        #  412 LOAD_CONST '{} ({})'
        #  414 LOAD_METHOD format
        #  436 LOAD_FAST alt_name
        # ... bytecode truncated ...
        pass

    def read_settings(self):
        use_mixed = read_bool_setting(self.settings, 'UseMixed', False)
        use_metric = read_bool_setting(self.settings, 'UseMetric', True)

    def write_settings(self):
        use_mixed = self.mixedUnits.isChecked()
        write_bool_setting(self.settings, 'UseMixed', use_mixed)

    def toggled_metric(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR metricUnits
        #   14 LOAD_METHOD isChecked
        #   36 PRECALL
        #   40 CALL
        #   50 POP_JUMP_FORWARD_IF_FALSE to 340
        #   52 LOAD_FAST self
        #   54 LOAD_ATTR unit_buttons
        #   64 LOAD_METHOD values
        #   86 PRECALL
        #   90 CALL
        #  100 GET_ITER
        #  102 FOR_ITER to 344
        #  104 STORE_FAST button_dict
        #  106 LOAD_FAST button_dict
        #  108 LOAD_CONST 'metric'
        #  110 BINARY_SUBSCR
        #  120 LOAD_METHOD setChecked
        #  142 LOAD_CONST True
        #  144 PRECALL
        #  148 CALL
        #  158 POP_TOP
        #  160 LOAD_FAST button_dict
        #  162 LOAD_CONST 'metric'
        #  164 BINARY_SUBSCR
        #  174 LOAD_METHOD setEnabled
        #  196 LOAD_CONST False
        #  198 PRECALL
        #  202 CALL
        #  212 POP_TOP
        #  214 LOAD_FAST button_dict
        #  216 LOAD_CONST 'us'
        #  218 BINARY_SUBSCR
        #  228 LOAD_METHOD setEnabled
        #  250 LOAD_CONST False
        #  252 PRECALL
        #  256 CALL
        #  266 POP_TOP
        #  268 LOAD_FAST button_dict
        #  270 LOAD_CONST 'alt'
        #  272 BINARY_SUBSCR
        #  282 POP_JUMP_FORWARD_IF_NONE to 338
        #  284 LOAD_FAST button_dict
        #  286 LOAD_CONST 'alt'
        #  288 BINARY_SUBSCR
        #  298 LOAD_METHOD setEnabled
        #  320 LOAD_CONST False
        #  322 PRECALL
        #  326 CALL
        #  336 POP_TOP
        #  338 JUMP_BACKWARD to 102
        #  340 LOAD_CONST None
        #  342 RETURN_VALUE
        #  344 LOAD_CONST None
        #  346 RETURN_VALUE
        pass

    def toggled_us(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR usUnits
        #   14 LOAD_METHOD isChecked
        #   36 PRECALL
        #   40 CALL
        #   50 POP_JUMP_FORWARD_IF_FALSE to 340
        #   52 LOAD_FAST self
        #   54 LOAD_ATTR unit_buttons
        #   64 LOAD_METHOD values
        #   86 PRECALL
        #   90 CALL
        #  100 GET_ITER
        #  102 FOR_ITER to 344
        #  104 STORE_FAST button_dict
        #  106 LOAD_FAST button_dict
        #  108 LOAD_CONST 'us'
        #  110 BINARY_SUBSCR
        #  120 LOAD_METHOD setChecked
        #  142 LOAD_CONST True
        #  144 PRECALL
        #  148 CALL
        #  158 POP_TOP
        #  160 LOAD_FAST button_dict
        #  162 LOAD_CONST 'metric'
        #  164 BINARY_SUBSCR
        #  174 LOAD_METHOD setEnabled
        #  196 LOAD_CONST False
        #  198 PRECALL
        #  202 CALL
        #  212 POP_TOP
        #  214 LOAD_FAST button_dict
        #  216 LOAD_CONST 'us'
        #  218 BINARY_SUBSCR
        #  228 LOAD_METHOD setEnabled
        #  250 LOAD_CONST False
        #  252 PRECALL
        #  256 CALL
        #  266 POP_TOP
        #  268 LOAD_FAST button_dict
        #  270 LOAD_CONST 'alt'
        #  272 BINARY_SUBSCR
        #  282 POP_JUMP_FORWARD_IF_NONE to 338
        #  284 LOAD_FAST button_dict
        #  286 LOAD_CONST 'alt'
        #  288 BINARY_SUBSCR
        #  298 LOAD_METHOD setEnabled
        #  320 LOAD_CONST False
        #  322 PRECALL
        #  326 CALL
        #  336 POP_TOP
        #  338 JUMP_BACKWARD to 102
        #  340 LOAD_CONST None
        #  342 RETURN_VALUE
        #  344 LOAD_CONST None
        #  346 RETURN_VALUE
        pass

    def toggled_mixed(self):
        # TODO: pycdc could not reconstruct this body.
        # Signature was recovered from the code object; default values may need manual repair.
        # Bytecode excerpt:
        #    0 RESUME
        #    2 LOAD_FAST self
        #    4 LOAD_ATTR mixedUnits
        #   14 LOAD_METHOD isChecked
        #   36 PRECALL
        #   40 CALL
        #   50 POP_JUMP_FORWARD_IF_FALSE to 286
        #   52 LOAD_FAST self
        #   54 LOAD_ATTR unit_buttons
        #   64 LOAD_METHOD values
        #   86 PRECALL
        #   90 CALL
        #  100 GET_ITER
        #  102 FOR_ITER to 290
        #  104 STORE_FAST button_dict
        #  106 LOAD_FAST button_dict
        #  108 LOAD_CONST 'metric'
        #  110 BINARY_SUBSCR
        #  120 LOAD_METHOD setEnabled
        #  142 LOAD_CONST True
        #  144 PRECALL
        #  148 CALL
        #  158 POP_TOP
        #  160 LOAD_FAST button_dict
        #  162 LOAD_CONST 'us'
        #  164 BINARY_SUBSCR
        #  174 LOAD_METHOD setEnabled
        #  196 LOAD_CONST True
        #  198 PRECALL
        #  202 CALL
        #  212 POP_TOP
        #  214 LOAD_FAST button_dict
        #  216 LOAD_CONST 'alt'
        #  218 BINARY_SUBSCR
        #  228 POP_JUMP_FORWARD_IF_NONE to 284
        #  230 LOAD_FAST button_dict
        #  232 LOAD_CONST 'alt'
        #  234 BINARY_SUBSCR
        #  244 LOAD_METHOD setEnabled
        #  266 LOAD_CONST True
        #  268 PRECALL
        #  272 CALL
        #  282 POP_TOP
        #  284 JUMP_BACKWARD to 102
        #  286 LOAD_CONST None
        #  288 RETURN_VALUE
        #  290 LOAD_CONST None
        #  292 RETURN_VALUE
        pass
