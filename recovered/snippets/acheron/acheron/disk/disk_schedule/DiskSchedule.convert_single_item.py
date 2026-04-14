# Source Generated with Decompyle++
# File: tmp6rwmpbbs.marshal (Python 3.11)

values = self.model_dump()
values['remote_sn'] = self._get_remote_sn(values['serial'])
del values['serial']
del values['cron_start']
del values['cron_timezone']
failure_delay = values.pop('failure_delay', None)
if failure_delay:
    values['failure_time'] = self.start_time + failure_delay
# WARNING: Decompyle incomplete
