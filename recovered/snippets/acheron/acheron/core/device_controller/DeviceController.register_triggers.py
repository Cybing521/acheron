# Source Generated with Decompyle++
# File: tmppy0h1u0o.marshal (Python 3.11)

old_triggers = self.registered_triggers.get(key)
if old_triggers == triggers:
    return None
self.registered_triggers[key] = None
self._update_trigger_names()
if self.calc_process:
    triggers = self._get_triggers()
    if self.triggers != triggers:
        self.triggers = triggers
        self.calc_process.change_triggers(triggers)
        return None
    return None
