# Source Generated with Decompyle++
# File: psd.pyc (Python 3.11)

import logging
import math
from typing import Literal
from matplotlib.backend_bases import MouseButton
from matplotlib.figure import Figure
from matplotlib.mlab import mlab
import numpy
from numpy.typing import NDArray
from PySide6 import QtGui, QtWidgets
from  import util
from  import export_csv
from  import export_script
logger = logging.getLogger(__name__)

def get_integrated_power(start_freq = None, end_freq = None, freqs = None, pxx = ('start_freq', float, 'end_freq', float, 'freqs', NDArray[numpy.float64], 'pxx', NDArray[numpy.float64], 'return', float)):
    start_index = max(0, numpy.searchsorted(freqs, start_freq, side = 'right').item() - 1)
    end_index = min(len(freqs), numpy.searchsorted(freqs, end_freq, side = 'left').item() + 1)
    dfreq = freqs[1] - freqs[0]
    integrated = numpy.sum(pxx[start_index:end_index]) * dfreq
    return integrated.item()


def add_amplitude_button(fig = None, ax = None, data = None):
    pass
# WARNING: Decompyle incomplete


def _stride_windows(x = None, n = None, noverlap = None):
    return numpy.lib.stride_tricks.sliding_window_view(x, n, axis = 0)[::n - noverlap].T


def do_psd(sequence, subchannel_index, NFFT, Fs = None, detrend = None, window = None, noverlap = ('sequence', list[util.Chunk], 'subchannel_index', int, 'NFFT', int, 'Fs', float, 'detrend', Literal[('mean', 'linear', 'none')], 'window', NDArray[numpy.float64], 'noverlap', int, 'return', tuple[(NDArray[numpy.float64], NDArray[numpy.float64])])):
    freqs = numpy.fft.rfftfreq(NFFT, 1 / Fs)
    windows = 0
    sums = numpy.zeros(freqs.shape)
    for _time, data, _start, _end in sequence:
        x = numpy.asarray(data[(:, subchannel_index)])
        if len(x) < NFFT:
            continue
        result = _stride_windows(x, NFFT, noverlap)
        result = mlab.detrend(result, detrend, axis = 0)
        result = numpy.asarray(result) * window.reshape((-1, 1))
        result = numpy.fft.rfft(result, n = NFFT, axis = 0)
        result = (numpy.conjugate(result) * result).real
        result /= (numpy.abs(window) ** 2).sum()
        windows += result.shape[1]
        result = result.sum(axis = 1)
        sums += result
        del result
        sums /= Fs = None
        sums /= windows
        return (sums, freqs)


def psd_analysis(parent = None):
    ret = util.load_batch(parent)
# WARNING: Decompyle incomplete


def single_channel_psd_analysis(parent = None):
    channel_index = None
    subchannel_index = None
    sampling_rate = None
    sequences = []
    units = []
    names = []
    files = set()
    ret = util.load_batch(parent)
# WARNING: Decompyle incomplete


def single_slice_psd_analysis(parent = None):
    pass
# WARNING: Decompyle incomplete


def overlaid_psd_analysis(parent = None):
    sequences = []
    names = []
    sampling_rates = []
    ret = util.load_batch(parent = parent)
# WARNING: Decompyle incomplete

