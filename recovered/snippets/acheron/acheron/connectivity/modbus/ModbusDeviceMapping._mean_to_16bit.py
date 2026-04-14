# Source Generated with Decompyle++
# File: tmpc7luk7ef.marshal (Python 3.11)


try:
    if value >= channel.maximum:
        return 65535
    if None <= channel.minimum:
        return 0
    ratio = (None - channel.minimum) / (channel.maximum - channel.minimum)
    return round(65535 * ratio)
except ValueError:
    return 0

