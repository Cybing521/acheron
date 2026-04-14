# Source Generated with Decompyle++
# File: tmpdlp3eck1.marshal (Python 3.11)


try:
    (triggers, trigger_names) = self._read_triggers(self.trigger_filename)
except Exception:
    message = 'Could not parse triggers'
    logger.exception(message)
    self.error.emit(message)
    return None


try:
    (single_schedule, cron_schedule, schedule_serials) = self._read_schedule_items(self.schedule_filename)
except Exception:
    message = 'Could not parse schedule items'
    logger.exception(message)
    self.error.emit(message)
    return None

self._check_missing_triggers(single_schedule, trigger_names)
self._check_missing_triggers(cron_schedule, trigger_names)
self.lock
serials = set(triggers) | schedule_serials
old_serials = set(self.controllers)
unused_serials = old_serials.difference(serials)
new_serials = serials.difference(old_serials)
# WARNING: Decompyle incomplete
