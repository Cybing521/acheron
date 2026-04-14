# Source Generated with Decompyle++
# File: tmppfoz3mz2.marshal (Python 3.11)

last_seen = datetime.datetime.now(datetime.timezone.utc)
results = self.device.get_radio_extra_scan_results()
scan_powers = { }
if device_info.radio_scan_power is True:
    power_max_queries = min(device_info.max_outgoing_param_length // 4, device_info.max_incoming_param_length)
    for i in range(0, len(results), power_max_queries):
        result_subset = results[i:i + power_max_queries]
        serials = result_subset()
        powers = self.device.get_radio_scan_power(serials)
        for sn, power in zip(serials, powers):
            if power != 127:
                scan_powers[sn] = power
            scans = []
            for r in results:
                power = scan_powers.get(r.serial_number, None)
                board_info = get_remote_board_info(r.serial_number, self.diskcache)
                scans.append(ScanResult(serial_number = r.serial_number, last_seen = last_seen, bootloader = bool(r.asphodel_type & asphodel.ASPHODEL_PROTOCOL_TYPE_BOOTLOADER), asphodel_type = r.asphodel_type, device_mode = r.device_mode, scan_strength = power, board_info = board_info))
                if scans:
                    self.status_pipe_lock
                    self.status_pipe.send((StreamStatus.SCAN_DATA, scans))
                    None(None, None)
                else:
                    with None:
                        if not (lambda .0: [ r.serial_number for r in .0 ]):
                            pass
return not scans
