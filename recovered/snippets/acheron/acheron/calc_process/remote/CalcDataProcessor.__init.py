# Source Generated with Decompyle++
# File: tmpringrkvl.marshal (Python 3.11)

self.device_decoder = decoder
self.channel_info = channel_info
self.data_pipe = data_pipe
self.logger = logger
self.is_shown = is_shown
self.channel_interval = channel_interval
self.plot_interval = plot_interval
self.fft_interval = fft_interval
self.current_channel_id = None
self.current_subchannel_index = None
self.mean_ringbuffers = { }
self.plot_ringbuffers = { }
self.fft_ringbuffers = { }
self.connectivity_pipe = None
self.connectivity_deques = { }
self.data_lock = threading.Lock()
self.trigger_lock = threading.Lock()
self.triggers_by_channel = { }
self.active_triggers = set()
self.change_triggers(triggers)
self.lost_packet_lock = threading.Lock()
self.lost_packet_count = 0
self.lost_packet_last_time = None
self.recent_lost_packet_count = 0
self.lost_packet_deque = deque()
self.last_lost_packet_update = None
self.stopped = threading.Event()
self.setup_decoder()
self.update_thread = threading.Thread(target = self.update_thread_run)
self.update_thread.start()
