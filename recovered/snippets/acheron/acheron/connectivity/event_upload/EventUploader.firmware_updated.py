# Source Generated with Decompyle++
# File: tmpgiw90a0s.marshal (Python 3.11)

event_data['success'] = success
if not success:
    description = 'Firmware Update Failed'
else:
    build_info = event_data.get('build_info')
    if build_info:
        description = f'''Firmware Update with {build_info}'''
    else:
        description = 'Firmware Update'
event = Event(serial_number = serial_number, category = 'Firmware Update', description = description, data = event_data)
if self.preferences.event_upload_enabled:
    self.event_queue.put_nowait(event)
    return None
