# Source Generated with Decompyle++
# File: tmpfg757izq.marshal (Python 3.11)

self.rerunButton.setEnabled(True)
if len(self.results) != len(self.tests):
    pass
(lambda .0: pass# WARNING: Decompyle incomplete
)(self.results.values()()) = sum
plural = 'failures' if failures != 1 else 'failure'
datetime.datetime.now(tz = datetime.timezone.utc) = self, self.test_log += f'''\n{failures} {plural}\n\n''', .test_log
dt_str = dt.strftime('%Y-%m-%dT%H:%M:%SZ')
end_message = f'''*** End of tests {dt_str} ***\n'''
self.testOutput.setPlainText(self.test_log)
self.save_test_log()
