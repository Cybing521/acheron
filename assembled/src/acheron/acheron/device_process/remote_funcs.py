# Source Generated with Decompyle++
# File: remote_funcs.pyc (Python 3.11)

from typing import Optional
import asphodel

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

def find_and_open_tcp_device(serial_number, location):
    # TODO: pycdc could not reconstruct this body.
    # Signature was recovered from the code object; default values may need manual repair.
    # Bytecode excerpt:
    #    0 RESUME
    #    2 LOAD_GLOBAL NULL + asphodel
    #   14 LOAD_ATTR find_tcp_devices
    #   24 PRECALL
    #   28 CALL
    #   38 STORE_FAST devices
    #   40 LOAD_FAST devices
    #   42 GET_ITER
    #   44 FOR_ITER to 212
    #   46 STORE_FAST device
    #   48 LOAD_FAST device
    #   50 LOAD_METHOD get_location_string
    #   72 PRECALL
    #   76 CALL
    #   86 STORE_FAST device_location_string
    #   88 LOAD_FAST device_location_string
    #   90 LOAD_FAST location
    #   92 COMPARE_OP ==
    #   98 POP_JUMP_FORWARD_IF_FALSE to 210
    #  100 LOAD_FAST device
    #  102 LOAD_METHOD tcp_get_advertisement
    #  124 PRECALL
    #  128 CALL
    #  138 STORE_FAST adv
    #  140 LOAD_FAST adv
    #  142 LOAD_ATTR serial_number
    #  152 LOAD_FAST serial_number
    #  154 COMPARE_OP ==
    #  160 POP_JUMP_FORWARD_IF_FALSE to 210
    #  162 LOAD_FAST device
    #  164 LOAD_METHOD open
    #  186 PRECALL
    #  190 CALL
    #  200 POP_TOP
    #  202 LOAD_FAST device
    #  204 SWAP
    #  206 POP_TOP
    #  208 RETURN_VALUE
    #  210 JUMP_BACKWARD to 44
    #  212 LOAD_CONST None
    #  214 RETURN_VALUE
    pass

def find_and_open_usb_device(location):
    devices = asphodel.find_usb_devices()
    for device in devices:
        device_location_string = device.get_location_string()
        if device_location_string == location:
            device.open()
            
            return None, device
        return None

def connect_and_open_tcp_device(host, port, timeout, serial):
    device = asphodel.create_tcp_device(host, port, timeout, serial)
    device.open()
    return device

def explode(device):
    raise Exception('Explosion')
