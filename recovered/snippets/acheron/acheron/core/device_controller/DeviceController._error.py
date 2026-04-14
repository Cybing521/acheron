# Source Generated with Decompyle++
# File: tmpztrx3kyr.marshal (Python 3.11)

if self.streaming:
    self.streaming = False
    if self.calc_process:
        self.calc_process.stop()
        if not self.proxy:
            self.calc_process.close()
            self.dispatcher.register_old_calc_process(self.calc_process)
            self.calc_process = None
    if self.proxy:
        self.proxy.send_job(self.stop_stream_controller_op)
self._disconnect_proxy()
self._streaming_disconnected(message)
self._remote_disconnected_cb()
