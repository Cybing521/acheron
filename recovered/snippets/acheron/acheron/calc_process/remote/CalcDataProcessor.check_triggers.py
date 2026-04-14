# Source Generated with Decompyle++
# File: tmppmgck6b0.marshal (Python 3.11)

for trigger in triggers:
    was_active = trigger.id in self.active_triggers
    if trigger.subchannel_index >= len(mean):
        continue
    if trigger.limit_type == LimitType.MEAN_HIGH_LIMIT:
        value = mean[trigger.subchannel_index]
        if was_active:
            active = value >= trigger.deactivate_limit
        else:
            active = value > trigger.activate_limit
    elif trigger.limit_type == LimitType.MEAN_LOW_LIMIT:
        value = mean[trigger.subchannel_index]
        if was_active:
            active = value <= trigger.deactivate_limit
        else:
            active = value < trigger.activate_limit
    elif trigger.limit_type == LimitType.STD_HIGH_LIMIT:
        value = std[trigger.subchannel_index]
        if was_active:
            active = value >= trigger.deactivate_limit
        else:
            active = value > trigger.activate_limit
    else:
        value = std[trigger.subchannel_index]
        if was_active:
            active = value <= trigger.deactivate_limit
        else:
            active = value < trigger.activate_limit
    if not active and was_active:
        self.active_triggers.add(trigger.id)
        self.triggers_changed = True
        continue
    if active and was_active:
        self.active_triggers.remove(trigger.id)
        self.triggers_changed = True
    return None
