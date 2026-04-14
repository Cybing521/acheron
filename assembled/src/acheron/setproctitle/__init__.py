# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''Allow customization of the process title.'''
import os
import sys
import logging
logger = logging.getLogger('setproctitle')
__version__ = '1.3.3'
# INVALID FROM DECOMPILER: __all__ = [
# INVALID FROM DECOMPILER:     'setproctitle',
# INVALID FROM DECOMPILER:     'getproctitle',
# INVALID FROM DECOMPILER:     'setthreadtitle',
# INVALID FROM DECOMPILER:     'getthreadtitle']

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

def setproctitle(title):
    logger.debug('setproctitle C module not available')

def getproctitle():
    logger.debug('setproctitle C module not available')
    return ' '.join(sys.argv)

def setthreadtitle(title):
    logger.debug('setproctitle C module not available')

def getthreadtitle():
    logger.debug('setproctitle C module not available')
    return ''
