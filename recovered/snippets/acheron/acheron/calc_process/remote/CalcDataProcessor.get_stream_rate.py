# Source Generated with Decompyle++
# File: tmpt2zqmlsk.marshal (Python 3.11)

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
