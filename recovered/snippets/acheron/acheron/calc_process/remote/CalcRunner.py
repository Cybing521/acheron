# Source Generated with Decompyle++
# File: tmpu0v5syn1.marshal (Python 3.11)


def __init__(self, packet_pipe, data_pipe, ctrl_pipe, serial_number = None, is_shown = None, settings = None, triggers = ('packet_pipe', Connection, 'data_pipe', Connection, 'ctrl_pipe', Connection, 'serial_number', str, 'is_shown', bool, 'settings', CalcSettings, 'triggers', set[Trigger])):
    self.packet_pipe = packet_pipe
    self.data_pipe = data_pipe
    self.ctrl_pipe = ctrl_pipe
    self.serial_number = serial_number
    self.is_shown = is_shown
    self.settings = settings
    self.triggers = triggers
    self.logger = DeviceLoggerAdapter(logger, self.serial_number)
    self.decoder = None
    self.data_processor = None
    self
    self


def create_decoder(self = None, device_info = None, active_streams = None):
    channel_info = { }
    streams = device_info.streams
    channels = device_info.channels
    info_list = []
    for i, stream in enumerate(streams):
        if i not in active_streams:
            continue
        channel_info_list = []
        ids = stream.channel_index_list[0:stream.channel_count]
        for channel_id in ids:
            channel_info_list.append(channels[channel_id])
            info_list.append((i, stream, channel_info_list))
            device_decoder = asphodel.nativelib.create_device_decoder(info_list, device_info.stream_filler_bits, device_info.stream_id_bits)
            for i, stream_decoder in enumerate(device_decoder.decoders):
                stream_id = device_decoder.stream_ids[i]
                for j, channel_decoder in enumerate(stream_decoder.decoders):
                    channel_id = stream_decoder.stream_info.channel_index_list[j]
                    channel = channels[channel_id]
                    channel_info[channel_id] = self.create_channel_info(device_info, stream_id, streams[stream_id], channel_id, channel, channel_decoder)
                    return (device_decoder, channel_info)


def create_channel_info(self, device_info, stream_id, stream = None, channel_id = None, channel = None, channel_decoder = ('device_info', DeviceInfo, 'stream_id', int, 'stream', AsphodelStreamInfo, 'channel_id', int, 'channel', AsphodelChannelInfo, 'channel_decoder', AsphodelNativeChannelDecoder, 'return', ChannelInformation)):
    rate_info = device_info.stream_rate_info[stream_id]
    samples = channel.samples
    channel_rate = samples * stream.rate
    sample_len = math.ceil(10 * channel_rate)
    sample_len = 2 ** math.ceil(math.log2(sample_len))
    if self.settings.downsample and sample_len > 32768:
        downsample_factor = samples
    else:
        downsample_factor = 1
    fft_sample_len = min(sample_len, 32768)
    return ChannelInformation(name = channel_decoder.channel_name, channel_id = channel_id, stream_id = stream_id, channel = channel, subchannel_names = channel_decoder.subchannel_names, rate_info = rate_info, samples = samples, rate = channel_rate, downsample_factor = downsample_factor, mean_len = math.ceil(1 * channel_rate), plot_len = sample_len // downsample_factor, fft_shortened = fft_sample_len != sample_len, fft_sample_len = fft_sample_len, fft_freq_axis = numpy.fft.rfftfreq(fft_sample_len, 1 / channel_rate), fft_size = fft_sample_len)


def stop_processing(self = None):
    self.decoder = None
    if self.data_processor:
        self.data_processor.stop_and_join()
        self.data_processor = None
        return None


def start_processing(self = None):
    self.stop_processing()
    (self.decoder, channel_info) = self.create_decoder(self.device_info, self.active_streams)
    self.data_pipe.send((CalcData.PROCESSING_START, self.device_info, self.active_streams, channel_info))
    self.data_processor = CalcDataProcessor(self.decoder, channel_info, self.data_pipe, self.logger, self.is_shown, self.settings.channel_interval, self.settings.plot_interval, self.settings.fft_interval, self.triggers)


def run(self = None):
    running = True
# WARNING: Decompyle incomplete

