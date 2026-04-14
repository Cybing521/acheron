# Source Generated with Decompyle++
# File: tmpumudskz6.marshal (Python 3.11)

from export_script import matplotlib_wrapper as matplotlib
import PySide6
matplotlib.use('Qt5Agg')
matplotlib.rcParams['agg.path.chunksize'] = 10000
matplotlib.rcParams['figure.constrained_layout.use'] = True
matplotlib.rcParams['image.interpolation'] = 'bilinear'
matplotlib.rcParams['image.resample'] = False

try:
    from version import version as __version__
except ImportError:
    __version__ = 'UNKNOWN'

if __name__ == '__main__':
    from  import __main__
    __main__.main()
    return None
