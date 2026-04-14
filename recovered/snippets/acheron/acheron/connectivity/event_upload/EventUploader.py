# Source Generated with Decompyle++
# File: tmpkz13h4j1.marshal (Python 3.11)


def __init__(self = None, preferences = None):
    self.preferences = preferences
    self.event_queue = queue.Queue()
    self.is_finished = threading.Event()
    self.upload_thread = threading.Thread(target = self._upload_loop)
    self.upload_thread.start()


def stop(self = None):
    self.is_finished.set()


def join(self = None):
    self.upload_thread.join()


def firmware_updated(self = None, serial_number = None, success = None, event_data = ('serial_number', str, 'success', bool, 'event_data', dict[(str, Any)], 'return', None)):
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


def calibration_finished(self = None, serial_number = None, event_data = None):
    event = Event(serial_number = serial_number, category = 'Calibration', description = 'Calibration', data = event_data)
    if self.preferences.event_upload_enabled:
        self.event_queue.put_nowait(event)
        return None


def _upload_event(self = None, event = None):
    pass
# WARNING: Decompyle incomplete


def _upload_loop(self = None):
    pass
# WARNING: Decompyle incomplete

