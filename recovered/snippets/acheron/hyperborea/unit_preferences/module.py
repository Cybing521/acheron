# Source Generated with Decompyle++
# File: tmp28jvm_ov.marshal (Python 3.11)

from dataclasses import dataclass
import math
from typing import Optional, TypedDict
from PySide6 import QtCore, QtWidgets
import asphodel
from preferences import read_bool_setting, write_bool_setting
from ui.ui_unit_preferences_widget import Ui_UnitPreferencesWidget

class UnitType(TypedDict):
    unit_strings: tuple[(str, str, str)] = 'UnitType'


class UnitButtonType(TypedDict):
    alt_setting: Optional[str] = 'UnitButtonType'

alternate_units: list[UnitType] = [
    {
        'unit_type': asphodel.UNIT_TYPE_WATT,
        'setting_name': 'UseHorsepower',
        'scale': 0.00134048,
        'offset': 0,
        'unit_strings': ('HP', 'HP', 'HP') },
    {
        'unit_type': asphodel.UNIT_TYPE_M_PER_S2,
        'setting_name': 'UseGForce',
        'scale': 0.101972,
        'offset': 0,
        'unit_strings': ('g', 'g', '<b>g</b>') },
    {
        'unit_type': asphodel.UNIT_TYPE_HZ,
        'setting_name': 'UseCPM',
        'scale': 60,
        'offset': 0,
        'unit_strings': ('CPM', 'CPM', 'CPM') },
    {
        'unit_type': asphodel.UNIT_TYPE_METER,
        'setting_name': 'UseInch',
        'scale': 39.3701,
        'offset': 0,
        'unit_strings': ('in', 'in', 'in') },
    {
        'unit_type': asphodel.UNIT_TYPE_GRAM,
        'setting_name': 'UseOunce',
        'scale': 0.035274,
        'offset': 0,
        'unit_strings': ('oz', 'oz', 'oz') },
    {
        'unit_type': asphodel.UNIT_TYPE_M3_PER_S,
        'setting_name': 'UseGPM',
        'scale': 15850.3,
        'offset': 0,
        'unit_strings': ('gal/min', 'gal/min', 'gal/min') },
    {
        'unit_type': asphodel.UNIT_TYPE_NEWTON_METER,
        'setting_name': 'UseLbfIn',
        'scale': 8.85075,
        'offset': 0,
        'unit_strings': ('lbf*in', b'lbf\xe2\x8b\x85in'.decode('utf-8'), 'lbf&#8901;in') }]
UnitOption = <NODE:12>()

def get_unit_options(unit_type = None, minimum = None, maximum = dataclass, resolution = ('unit_type', int, 'minimum', float, 'maximum', float, 'resolution', float, 'return', list[UnitOption])):
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
# WARNING: Decompyle incomplete


def get_default_option(settings = None, unit_type = None, unit_options = None):
    use_mixed = read_bool_setting(settings, 'UseMixed', False)
    if use_mixed:
        for unit_option in unit_options:
            setting_name = unit_option.alt_setting_name
            if setting_name and read_bool_setting(settings, setting_name, False):
                
                return None, unit_option
            'UseMetricType{}'.format(unit_type) = read_bool_setting(settings, 'UseMetric', True)
            use_metric = read_bool_setting(settings, setting_name, use_metric_overall)
    use_metric = read_bool_setting(settings, 'UseMetric', True)
    for unit_option in unit_options:
        if use_metric:
            if unit_option.metric:
                
                return None, unit_option
        if unit_option.non_metric:
            
            return None, unit_option
        raise ValueError('No valid unit options')


def create_unit_formatter(settings, unit_type = None, minimum = None, maximum = None, resolution = ('settings', QtCore.QSettings, 'unit_type', int, 'minimum', float, 'maximum', float, 'resolution', float, 'return', asphodel.AsphodelNativeUnitFormatter)):
    unit_options = get_unit_options(unit_type, minimum, maximum, resolution)
    option = get_default_option(settings, unit_type, unit_options)
    return option.unit_formatter


class UnitPreferencesWidget(QtWidgets.QWidget, Ui_UnitPreferencesWidget):
    pass
# WARNING: Decompyle incomplete

