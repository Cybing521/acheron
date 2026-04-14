# Source Generated with Decompyle++
# File: tmpwrwfq596.marshal (Python 3.11)

turn_on = False
turn_off = False
self.lock
if needed:
    if controller in self.rf_power_needed:
        None(None, None)
        return None
    was_needed = None(self.rf_power_needed)
    self.rf_power_needed.add(controller)
    if not was_needed:
        turn_on = True
    elif controller in self.rf_power_needed:
        self.rf_power_needed.discard(controller)
        if not self.rf_power_needed:
            turn_off = True
        else:
            None(None, None)
            return None
        None(None, None)
    else:
        with None:
            if not None:
                pass
if turn_on:
    self.enable_all_rf_power()
    return None
if None:
    self.disable_all_rf_power()
    return None
