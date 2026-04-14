# Source Generated with Decompyle++
# File: tmp8m8ku0qv.marshal (Python 3.11)

for device in nativelib.find_tcp_devices():
    adv = device.tcp_get_advertisement()
    if adv.serial_number == serial:
        
        return None, device
    for None in nativelib.find_usb_devices():
        if device.get_serial_number() == serial:
            device.close()
            
            return None, device
        except AsphodelError:
            device.close()
            continue
        device.close()
        device.close()
        return None
