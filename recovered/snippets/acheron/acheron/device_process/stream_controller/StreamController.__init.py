# Source Generated with Decompyle++
# File: tmpo7zmdkt6.marshal (Python 3.11)

self.device = device
self.device_lock = device_lock
self.logger = logger
self.settings = settings
self.main_schedule_id = main_schedule_id
self.diskcache = diskcache
self.ctrl_pipe = ctrl_pipe
self.packet_pipe = packet_pipe
self.device.set_error_callback(self._device_error_callback)
self.device_info_logger = proxy_remote.get_device_logger(device_info_logger, device)
self.rgb_manager = RGBManager(device, settings.auto_rgb, self._rgb_callback)
self
self

try:
    controller = self.device.stream_controller
    self.parent_controller = controller
    remote_info = self.device.remote_info
    self.parent_controller.register_subcontroller_locked(self)
    self.schedule = self.parent_controller.get_remote_schedule(schedule_items, remote_info)
except AttributeError:
    self.parent_controller = None
    self.schedule = Schedule(schedule_items, active_triggers)

self.ctrl_queue = Queue()
self.status_pipe_lock = threading.Lock()
self.status_pipe = status_pipe
self.finished = threading.Event()
self.disconnected = threading.Event()
self.reset_function = None
self.hw_tests = None
self.rf_test_params = None
self.remote_wrapper = None
self.subcontroller = None
self.poll_thread = threading.Thread(target = self.poll_thread_run)
self.stream_thread = threading.Thread(target = self.stream_thread_run)
self.packet_thread = None
self.check_connection_thread = None
self.radio_thread = None
self.rf_power_thread = None
self.radio_queue = Queue()
self.writer_lock = threading.Lock()
self.writers = { }
self.stop_lock = threading.Lock()
self.stop_called = False
self.stop_finished = threading.Event()
self.background_join_deque = deque()
self.background_join_thread = threading.Thread(target = self.background_join_run)
self.background_join_thread.start()
