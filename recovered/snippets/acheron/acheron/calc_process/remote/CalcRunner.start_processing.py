# Source Generated with Decompyle++
# File: tmp4plol8sq.marshal (Python 3.11)

self.stop_processing()
(self.decoder, channel_info) = self.create_decoder(self.device_info, self.active_streams)
self.data_pipe.send((CalcData.PROCESSING_START, self.device_info, self.active_streams, channel_info))
self.data_processor = CalcDataProcessor(self.decoder, channel_info, self.data_pipe, self.logger, self.is_shown, self.settings.channel_interval, self.settings.plot_interval, self.settings.fft_interval, self.triggers)
