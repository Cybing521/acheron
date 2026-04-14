# Source Generated with Decompyle++
# File: tmp84xn6keq.marshal (Python 3.11)

trigger_names = set()
for key, triggers in self.registered_triggers.items():
    if key != 'alerts':
        (lambda .0: pass# WARNING: Decompyle incomplete
)(triggers())
    new_trigger_names = frozenset(trigger_names)
    if new_trigger_names != self.trigger_names:
        inactive = new_trigger_names.difference(self.last_emitted_active_triggers)
        self.active_triggers_changed.emit(self, self.last_emitted_active_triggers, inactive)
        self.trigger_names = new_trigger_names
        return None
    return trigger_names.update
