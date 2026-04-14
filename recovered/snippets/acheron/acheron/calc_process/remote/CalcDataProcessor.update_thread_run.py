# Source Generated with Decompyle++
# File: tmpfvsguzrz.marshal (Python 3.11)

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

