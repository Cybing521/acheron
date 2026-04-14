# Source Generated with Decompyle++
# File: tmpr61am7ir.marshal (Python 3.11)

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
