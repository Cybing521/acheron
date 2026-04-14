# Source Generated with Decompyle++
# File: tmphgo9w6ji.marshal (Python 3.11)

for channel_id, alert_actions in self.channel_alert_actions.items():
    for i, alert_action in enumerate(alert_actions):
        alert_limits = self.controller.device_prefs.get_alert_limits(channel_id, i)
        if alert_limits:
            alert_action.setIcon(QtGui.QIcon.fromTheme('signal_flag_red'))
            continue
        alert_action.setIcon(QtGui.QIcon.fromTheme('signal_flag_white'))
        return None
