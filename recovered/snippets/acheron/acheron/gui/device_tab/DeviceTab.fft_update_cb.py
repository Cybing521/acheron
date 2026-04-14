# Source Generated with Decompyle++
# File: tmpp1wpchms.marshal (Python 3.11)

selected_channel_id = self.get_current_channel_id()
if channel_id != selected_channel_id:
    return None
selected_subchannel_index = None.fftSubchannelComboBox.currentIndex()
if subchannel_id != selected_subchannel_index:
    return None

try:
    unit_formatter = self.channel_unit[channel_id].unit_formatter
except KeyError:
    return None

if numpy.ndim(fft_data) == 0:
    if not self.buffering:
        self.bufferingLabel.setVisible(True)
        self.buffering = True
    
    try:
        percent = int(100 * fft_data)
        text = f'''Buffering {percent}%'''
    except Exception:
        text = 'Buffering'

    self.bufferingLabel.setText(text)
    return None
if self.buffering:
    self.bufferingLabel.setVisible(False)
    self.buffering = False
fft_data *= unit_formatter.conversion_scale
self.fft_curve.setData(fft_freqs, fft_data)
