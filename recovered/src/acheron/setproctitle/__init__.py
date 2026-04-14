# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''Allow customization of the process title.'''
import os
import sys
import logging
logger = logging.getLogger('setproctitle')
__version__ = '1.3.3'
__all__ = [
    'setproctitle',
    'getproctitle',
    'setthreadtitle',
    'getthreadtitle']

def setproctitle(title = None):
    logger.debug('setproctitle C module not available')


def getproctitle():
    logger.debug('setproctitle C module not available')
    return ' '.join(sys.argv)


def setthreadtitle(title = None):
    logger.debug('setproctitle C module not available')


def getthreadtitle():
    logger.debug('setproctitle C module not available')
    return ''


try:
    from  import _setproctitle
    setproctitle = _setproctitle.setproctitle
    getproctitle = _setproctitle.getproctitle
    setthreadtitle = _setproctitle.setthreadtitle
    getthreadtitle = _setproctitle.getthreadtitle
except ImportError:
    e = None
    if os.environ.get('SPT_DEBUG', ''):
        logging.basicConfig()
        logger.setLevel(logging.DEBUG)
    logger.debug('failed to import setproctitle: %s', e)
    e = None
    del e
except:
    e = None
    del e

if sys.platform == 'darwin':
    getproctitle()
    return None
