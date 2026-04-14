# Source Generated with Decompyle++
# File: tmpvfefcfdk.marshal (Python 3.11)


try:
    return self.schedules[serial_numbers]
except KeyError:
    pass

if len(serial_numbers) == 0:
    raise ValueError('No serial numbers provided')
if len(serial_numbers) == 1:
    device_schedule = DeviceSchedule(None)
elif len(serial_numbers) == 2:
    parent = self.get_schedule(serial_numbers[:-1])
    device_schedule = DeviceSchedule(parent)
else:
    raise ValueError('Too many serial numbers provided')
self.schedules[serial_numbers] = device_schedule
return device_schedule
