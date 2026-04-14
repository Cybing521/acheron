# Source Generated with Decompyle++
# File: tmp0d346x3g.marshal (Python 3.11)

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
