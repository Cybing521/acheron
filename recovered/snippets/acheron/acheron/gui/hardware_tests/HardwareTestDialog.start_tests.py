# Source Generated with Decompyle++
# File: tmpuarfu82e.marshal (Python 3.11)

self.rerunButton.setEnabled(False)
self.results = { }
self.controller.run_hardware_tests(self.tests, self)
dt = datetime.datetime.now(tz = datetime.timezone.utc)
dt_str = dt.strftime('%Y-%m-%dT%H:%M:%SZ')
start_message = f'''*** Start of tests {dt_str} ***\n\n'''
self.test_log = start_message
self.testOutput.setPlainText(self.test_log)
