# Source Generated with Decompyle++
# File: tmp1_1yz42t.marshal (Python 3.11)

self.all_pipes.discard(pipe)
self.pipe_callbacks.pop(pipe, None)
for serial_number, other_pipe in self.device_pipes.items():
    if pipe == other_pipe:
        del self.device_pipes[serial_number]
        return None
    return None
