# Source Generated with Decompyle++
# File: tmpgpxpccja.marshal (Python 3.11)

self.remove_device_mapping(serial_number)
t = (register_offset, device_mapping)
self.device_mappings[serial_number] = t
overlap_serials = set()
intervals = set()
for block in range(7):
    if block < 6:
        block_length = device_mapping.channel_count
    else:
        block_length = 2
    start_address = 1000 * block + register_offset
    end_address = start_address + block_length * 2 - 1
    interval = Interval(start_address, end_address, t)
    intervals.add(interval)
    overlap_intervals = self.interval_tree[start_address:end_address]
    for overlap_interval in overlap_intervals:
        overlapping_device_mapping = cast(ModbusDeviceMapping, overlap_interval.data[1])
        overlap_serials.add(overlapping_device_mapping.serial_number)
        self.interval_tree.add(interval)
        self.device_intervals[serial_number] = intervals
        device_logger = DeviceLoggerAdapter(logger, serial_number)
        if overlap_serials:
            other_devices = ', '.join(sorted(overlap_serials))
            device_logger.warning('Modbus addresses overlap with: %s', other_devices)
device_logger.info('Modbus starting (offset %s)', register_offset)
