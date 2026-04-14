# Source Generated with Decompyle++
# File: tmpj4oh8u3g.marshal (Python 3.11)


def __init__(self, decoder, channel_info, data_pipe, logger, is_shown, channel_interval = None, plot_interval = None, fft_interval = None, triggers = ('decoder', AsphodelNativeDeviceDecoder, 'channel_info', dict[(int, ChannelInformation)], 'data_pipe', Connection, 'logger', DeviceLoggerAdapter, 'is_shown', bool, 'channel_interval', float, 'plot_interval', float, 'fft_interval', float, 'triggers', set[Trigger])):
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


def stop_and_join(self = None):
    self.stopped.set()
    self.update_thread.join()
# WARNING: Decompyle incomplete


def set_connectivity_pipe(self = None, pipe = None):
    self.connectivity_pipe = pipe


def process_connectivity(self = None):
    pass
# WARNING: Decompyle incomplete


def setup_decoder(self = None):
    self.device_decoder.set_unknown_id_callback(self.unknown_id_cb)
    channel_decoders = { }
    for i, stream_decoder in enumerate(self.device_decoder.decoders):
        stream_id = self.device_decoder.stream_ids[i]
        lost_packet_cb = self.create_lost_packet_callback(stream_id)
        stream_decoder.set_lost_packet_callback(lost_packet_cb)
        for j, channel_decoder in enumerate(stream_decoder.decoders):
            channel_id = stream_decoder.stream_info.channel_index_list[j]
            channel_decoders[channel_id] = channel_decoder
            for channel_id in sorted(channel_decoders.keys()):
                channel_decoder = channel_decoders[channel_id]
                self.setup_channel(channel_id, channel_decoder)
                return None


def setup_channel(self = None, channel_id = None, channel_decoder = None):
    pass
# WARNING: Decompyle incomplete


def create_lost_packet_callback(self = None, stream_id = None):
    pass
# WARNING: Decompyle incomplete


def update_lost_packets(self = None):
    lost_count_too_old = 0
    now = datetime.datetime.now(datetime.timezone.utc)
    twenty_secs_ago = now - datetime.timedelta(seconds = 20)
    if len(self.lost_packet_deque):
        (lost_dt, lost) = self.lost_packet_deque[0]
        if lost_dt < twenty_secs_ago:
            lost_count_too_old += lost
            self.lost_packet_deque.popleft()
        
# WARNING: Decompyle incomplete


def get_stream_rate(self = None, rate_info = None):
    if rate_info.available:
        rate_channel_id = rate_info.channel_index
        ringbuffer = self.fft_ringbuffers[rate_channel_id]
        if len(ringbuffer) != 0:
            rate_data = ringbuffer.get_contents()
            raw_rate = numpy.average(rate_data)
            if not math.isfinite(raw_rate):
                return None
            stream_rate = None * rate_info.scale + rate_info.offset
            if rate_info.invert:
                if stream_rate != 0:
                    stream_rate = 1 / stream_rate
                else:
                    stream_rate = 0
            return stream_rate
        return None


def change_triggers(self = None, triggers = None):
    triggers_by_channel = { }
    for trigger in triggers:
        channel_triggers = triggers_by_channel.get(trigger.channel_id)
        if channel_triggers:
            channel_triggers.add(trigger)
            continue
        triggers_by_channel[trigger.channel_id] = set((trigger,))
        available_ids = (lambda .0: pass# WARNING: Decompyle incomplete
)(triggers())
        self.trigger_lock
        self.triggers_by_channel = triggers_by_channel
        active_count = len(self.active_triggers)
        self.active_triggers.intersection_update(available_ids)
        if len(self.active_triggers) != active_count:
            self.data_lock
            self.data_pipe.send((CalcData.ACTIVE_TRIGGERS_CHANGED, self.active_triggers))
            None(None, None)
        else:
            with None:
                if not set:
                    pass
    None(None, None)
    return None
    with None:
        if not None:
            pass


def check_triggers(self = None, triggers = None, mean = None, std = ('triggers', set[Trigger], 'mean', NDArray[numpy.float64], 'std', NDArray[numpy.float64], 'return', None)):
    for trigger in triggers:
        was_active = trigger.id in self.active_triggers
        if trigger.subchannel_index >= len(mean):
            continue
        if trigger.limit_type == LimitType.MEAN_HIGH_LIMIT:
            value = mean[trigger.subchannel_index]
            if was_active:
                active = value >= trigger.deactivate_limit
            else:
                active = value > trigger.activate_limit
        elif trigger.limit_type == LimitType.MEAN_LOW_LIMIT:
            value = mean[trigger.subchannel_index]
            if was_active:
                active = value <= trigger.deactivate_limit
            else:
                active = value < trigger.activate_limit
        elif trigger.limit_type == LimitType.STD_HIGH_LIMIT:
            value = std[trigger.subchannel_index]
            if was_active:
                active = value >= trigger.deactivate_limit
            else:
                active = value > trigger.activate_limit
        else:
            value = std[trigger.subchannel_index]
            if was_active:
                active = value <= trigger.deactivate_limit
            else:
                active = value < trigger.activate_limit
        if not active and was_active:
            self.active_triggers.add(trigger.id)
            self.triggers_changed = True
            continue
        if active and was_active:
            self.active_triggers.remove(trigger.id)
            self.triggers_changed = True
        return None


def update_channels(self = None):
    self.trigger_lock
    self.triggers_changed = False
# WARNING: Decompyle incomplete


def update_plots(self = None):
    if not self.is_shown:
        return None
    channel_id = None.current_channel_id
# WARNING: Decompyle incomplete


def update_ffts(self = None):
    if not self.is_shown:
        return None
    channel_id = None.current_channel_id
# WARNING: Decompyle incomplete


def set_is_shown(self = None, is_shown = None):
    self.is_shown = is_shown
    if is_shown:
        self.update_plots()
        self.update_ffts()
        return None


def plot_change(self = None, channel_id = None, subchannel_index = None):
    if channel_id == -1:
        channel_id = None
    if subchannel_index == -1:
        subchannel_index = None
    self.current_channel_id = channel_id
    self.current_subchannel_index = subchannel_index


def reset_lost_packets(self = None):
    self.lost_packet_deque.clear()
    self.lost_packet_lock
    self.recent_lost_packet_count = 0
    None(None, None)
    return None
    with None:
        if not None:
            pass


def unknown_id_cb(self = None, unknown_id = None):
    self.data_lock
    self.data_pipe.send((CalcData.UNKNOWN_ID, unknown_id))
    None(None, None)
    return None
    with None:
        if not None:
            pass


def update_thread_run(self = None):
    update_funcs = []
    if self.fft_interval:
        update_funcs.append((self.update_ffts, self.fft_interval))
    if self.plot_interval:
        update_funcs.append((self.update_plots, self.plot_interval))
    if self.channel_interval:
        update_funcs.append((self.update_channels, self.channel_interval))
        update_funcs.append((self.update_lost_packets, self.channel_interval))
    if not update_funcs:
        return None
    next_run = [
        None.monotonic()] * len(update_funcs)
    
    try:
        now = time.monotonic()
        for func, interval in enumerate(update_funcs):
            if next_run[i] <= now:
                func()
                if next_run[i] <= now:
                    now + interval = None
            wait_time = min(next_run) - time.monotonic()
            if wait_time < 0:
                wait_time = 0
        if self.stopped.wait(wait_time):
            self.logger.debug('Calc process update thread stopped')
            return None
    except Exception:
        self.logger.exception('Unhandled exception in update_thread_run')
        return None


