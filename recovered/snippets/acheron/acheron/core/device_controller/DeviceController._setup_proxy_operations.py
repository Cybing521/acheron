# Source Generated with Decompyle++
# File: tmp7ypie99z.marshal (Python 3.11)

self.start_stream_controller_op = DeviceOperation(start_stream_controller)
self.stop_stream_controller_op = DeviceOperation(stop_stream_controller)
self.stop_stream_controller_op.completed.connect(self._stop_stream_controller_cb)
self.close_device_op = SimpleDeviceOperation('close')
