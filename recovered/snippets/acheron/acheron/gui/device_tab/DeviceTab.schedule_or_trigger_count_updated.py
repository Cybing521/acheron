# Source Generated with Decompyle++
# File: tmp78jf8lml.marshal (Python 3.11)

trigger_count = self.controller.trigger_count
schedule_count = self.controller.schedule_count
if trigger_count == 1:
    trigger_str = self.tr('1 trigger')
elif trigger_count > 1:
    trigger_str = self.tr('{} triggers').format(trigger_count)
else:
    trigger_str = ''
if schedule_count == 1:
    schedule_str = self.tr('1 schedule item')
elif schedule_count > 1:
    schedule_str = self.tr('{} schedule items').format(schedule_count)
else:
    schedule_str = ''
self.tree_item.setText(6, str(schedule_count))
if trigger_str and schedule_str:
    self.scheduleLabel.setText(trigger_str + ', ' + schedule_str)
    self.scheduleLabel.setVisible(True)
    return None
if None:
    self.scheduleLabel.setText(trigger_str)
    self.scheduleLabel.setVisible(True)
    return None
if None:
    self.scheduleLabel.setText(schedule_str)
    self.scheduleLabel.setVisible(True)
    return None
None.scheduleLabel.setText('')
self.scheduleLabel.setVisible(False)
