# Source Generated with Decompyle++
# File: tmp57g6rh4q.marshal (Python 3.11)

self.channel_data[channel_id] = (mean, std_dev)
unit_formatter = self.channel_unit[channel_id].unit_formatter
mean_scaled = mean * unit_formatter.conversion_scale + unit_formatter.conversion_offset
std_dev_scaled = std_dev * unit_formatter.conversion_scale
for i, fields in enumerate(self.subchannel_fields[channel_id]):
    (mean_field, std_dev_field) = fields
    mean_string = unit_formatter.format_utf8(mean_scaled[i])
    mean_field.setText(mean_string)
    std_dev_string = unit_formatter.format_utf8(std_dev_scaled[i])
    std_dev_field.setText(std_dev_string)
    return None
