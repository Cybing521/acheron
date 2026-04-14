# Source Generated with Decompyle++
# File: tmp7evhyw_3.marshal (Python 3.11)


try:
    if value <= 0:
        return 0
    std_max = (None.maximum - channel.minimum) / 2
    if value >= std_max:
        return 65535
    return None((value / std_max) * 65535)
except ValueError:
    return 0

