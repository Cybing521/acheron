# Source Generated with Decompyle++
# File: tmp10m1afsj.marshal (Python 3.11)

if active_triggers:
    active_trigger_str = self.tr('Active triggers: {}')
    s = active_trigger_str.format(', '.join(sorted(active_triggers, key = str.casefold)))
    self.activeTriggerLabel.setText(s)
    self.activeTriggerLabel.setVisible(True)
    return None
None.activeTriggerLabel.setVisible(False)
