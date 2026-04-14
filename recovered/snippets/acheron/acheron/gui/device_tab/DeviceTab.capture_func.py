# Source Generated with Decompyle++
# File: tmp636ba95r.marshal (Python 3.11)


try:
    (mean, std_dev) = self.channel_data[channel_id]
    return (mean, std_dev)
except KeyError:
    nanarray = numpy.array([
        [
            numpy.nan]])
    return 

