# Source Generated with Decompyle++
# File: tmpd_1fkxyy.marshal (Python 3.11)

import binascii
import io
import json
import logging
import lzma
import os
from typing import Any, Callable, Optional
import asphodel
from asphodel.device_info import DeviceInfo
BootloaderCallback = Callable[([
    int,
    int,
    str], None)]

def get_default_file(device_info = None, base_dir = None):
    if not base_dir:
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'))
    
    try:
        import firmutil.repo_info as firmutil
        (boardname, boardrev) = device_info.board_info
        repo = firmutil.repo_info.get_repo_from_board(boardname, boardrev)
    except ImportError:
        repo = None

    if not repo:
        repo = device_info.repo_name
    if not repo:
        return ('', '')
    file_dir = None.path.abspath(os.path.join(base_dir, f'''{repo}/firmware/build'''))
    if not os.path.exists(file_dir):
        return ('', '')
    for file_name in None.listdir(file_dir):
        if os.path.splitext(file_name)[1] == '.firmware':
            
            return None, (file_dir, file_name)
        return ('', '')


def decode_firm_file(firm_file = None):
    lzma_file = lzma.LZMAFile(firm_file)
    f = io.TextIOWrapper(lzma_file)
    None(None, None)
    None(None, None)
    return 
    with None:
        if not None, json.load(f), :
            pass
    None(None, None)
    return None
    with None:
        if not None:
            pass


def decode_firm_bytes(firm_bytes = None):
    json_str = lzma.decompress(firm_bytes).decode()
    return json.loads(json_str)


def already_programmed(firm_data = None, device_info = None):
    if device_info.supports_bootloader:
        return False
    if None.get('build_info') != device_info.build_info:
        return False
    if None.get('build_date') != device_info.build_date:
        return False
    if None.get('application', False) is not True:
        return False
    if None.get('bootloader', False) is not False:
        return False


def do_bootload_page(device, done_bytes, page_data, block_sizes = None, total_bytes = None, message = None, callback = ('device', asphodel.AsphodelNativeDevice, 'done_bytes', int, 'page_data', bytes, 'block_sizes', tuple[(int, ...)], 'total_bytes', int, 'message', str, 'callback', BootloaderCallback, 'return', None)):
    pass
# WARNING: Decompyle incomplete


def do_bootload_pass(device, firm_data, block_sizes = None, verify_size = None, total_bytes = None, callback = ('device', asphodel.AsphodelNativeDevice, 'firm_data', dict[(str, Any)], 'block_sizes', tuple[(int, ...)], 'verify_size', int, 'total_bytes', int, 'callback', BootloaderCallback, 'return', None)):
    done_bytes = 0
    for page_info in firm_data['data']:
        page_number = page_info[0]
        nonce = binascii.a2b_hex(page_info[1])
        page_data = binascii.a2b_hex(page_info[2])
        digest = binascii.a2b_hex(page_info[3])
        message = 'Writing Page {}'.format(page_number)
        callback(done_bytes, total_bytes, message)
        device.start_bootloader_page(page_number, nonce)
        device.verify_bootloader_page(digest)
        different = False
    except asphodel.AsphodelError:
        e = None
        if e.args[1] == 'ERROR_CODE_INVALID_DATA':
            different = True
        else:
            raise 
        e = None
        del e
    except:
        e = None
        del e
    if different:
        device.start_bootloader_page(page_number, nonce)
        do_bootload_page(device, done_bytes, page_data, block_sizes, total_bytes, message, callback)
        device.finish_bootloader_page(digest)
    done_bytes += len(page_data)
    continue
    for page_info in firm_data['data']:
        page_number = page_info[0]
        nonce = binascii.a2b_hex(page_info[1])
        digest = binascii.a2b_hex(page_info[3])
        message = 'Verifying Page {}'.format(page_number)
        callback(done_bytes, total_bytes, message)
        device.start_bootloader_page(page_number, nonce)
        device.verify_bootloader_page(digest)
        done_bytes += verify_size
        return None


def do_bootload(device, serial_number = None, logger = None, firm_data = None, callback = ('device', asphodel.AsphodelNativeDevice, 'serial_number', str, 'logger', logging.LoggerAdapter, 'firm_data', dict[(str, Any)], 'callback', BootloaderCallback, 'return', None)):
    tries = 3
    block_sizes = None
    write_bytes = (lambda .0: pass# WARNING: Decompyle incomplete
)(firm_data['data']())
    if not device.supports_bootloader_commands():
        callback(0, 0, 'Switching to bootloader...')
        device.bootloader_jump()
        device.reconnect(bootloader = True, serial_number = serial_number)
        logger.info('Switched to bootloader')
# WARNING: Decompyle incomplete

