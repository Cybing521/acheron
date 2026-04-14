# Source Generated with Decompyle++
# File: tmpecjyln88.marshal (Python 3.11)

was_manually_controlled = MANUAL_CONTROL in self.parties
self.parties.update(parties)
if not MANUAL_CONTROL in parties or was_manually_controlled:
    self._update_schedule_items()
    self.manual_control_changed.emit(True)
    return None
return None
