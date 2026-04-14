# Source Generated with Decompyle++
# File: tmpvlj47gj0.marshal (Python 3.11)

values = self.model_dump()
values['remote_sn'] = self._get_remote_sn(values['serial'])
del values['serial']
del values['cron_start']
del values['cron_timezone']
values['start_time'] = start_time
failure_delay = values.pop('failure_delay', None)
if failure_delay:
    values['failure_time'] = start_time + failure_delay
id = self.get_base_id() + ' ' + start_time.isoformat()
# WARNING: Decompyle incomplete
