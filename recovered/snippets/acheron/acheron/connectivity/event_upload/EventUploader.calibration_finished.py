# Source Generated with Decompyle++
# File: tmpuzy8lp8n.marshal (Python 3.11)

event = Event(serial_number = serial_number, category = 'Calibration', description = 'Calibration', data = event_data)
if self.preferences.event_upload_enabled:
    self.event_queue.put_nowait(event)
    return None
