# Source Generated with Decompyle++
# File: tmp2zijyfv5.marshal (Python 3.11)


try:
    unscaled_captured_mag = self.capturedMagnitude.value() / self.cal.calibration_info.scale
    unscaled_captured_offset = (self.capturedOffset.value() - self.cal.calibration_info.offset) / self.cal.calibration_info.scale
    scale = self.actualMagnitude.value() / unscaled_captured_mag
    if scale == 0:
        return None
    offset = None.actualOffset.value() - unscaled_captured_offset * scale
    return (scale, offset)
except ZeroDivisionError:
    return None

