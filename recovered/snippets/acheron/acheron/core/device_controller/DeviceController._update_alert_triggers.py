# Source Generated with Decompyle++
# File: tmplc2a6xnq.marshal (Python 3.11)

triggers = set()
alert_triggers = { }
alert_limits = self.device_prefs.get_all_alert_limits()
for limit_type, channel_id, subchannel_index, value in alert_limits:
    id = f'''_alert_{channel_id}_{subchannel_index}_{limit_type}'''
    trigger = Trigger(id = id, channel_id = channel_id, subchannel_index = subchannel_index, limit_type = limit_type, activate_limit = value, deactivate_limit = value)
    triggers.add(trigger)
    alert_triggers[id] = trigger
    self.alert_triggers = alert_triggers
    self.register_triggers('alerts', triggers)
    return None
