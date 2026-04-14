# Source Generated with Decompyle++
# File: tmpx1x6vfp5.marshal (Python 3.11)

if party not in self.parties:
    return None
was_manually_controlled = None in self.parties
self.parties.discard(party)
if self.parties:
    if party == MANUAL_CONTROL or was_manually_controlled:
        self._update_schedule_items()
        self.manual_control_changed.emit(False)
        return None
    return None
return None
self.dispatcher.stop_controller(self)
