# Source Generated with Decompyle++
# File: tmp_qq4jt28.marshal (Python 3.11)

if self.remote_target_serial and MANUAL_CONTROL in self.parties:
    schedule_item = ScheduleItem(id = '_remote', remote_sn = self.remote_target_serial, remote_bootloader = self.remote_target_bootloader, start_time = None, collection_time = None, stop_time = None, duration = None, failure_time = None, output_config = None)
    self.schedule.add_item('_remote', schedule_item)
    return None
None.schedule.clear_partition('_remote')
