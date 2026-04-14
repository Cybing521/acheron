# Source Generated with Decompyle++
# File: tmpsrt9mppe.marshal (Python 3.11)

keys = '|'.join(self._alert_key_types.values())
pattern = re.compile('AlertCh(\\d+)_(\\d+)/(' + keys + ')Enabled')
parsed_values = []
for setting_name in self.settings.allKeys():
    match = pattern.match(setting_name)
    if not match:
        continue
    enabled = read_bool_setting(self.settings, setting_name, False)
    if not enabled:
        continue
    (channel_id, subchannel_index, key) = match.groups()
    v_key = f'''AlertCh{channel_id}_{subchannel_index}/{key}Value'''
    value = self._get_alert_value(v_key)
    if not value:
        continue
    parsed_values.append((self._key_to_limit_type(key), int(channel_id), int(subchannel_index), value))
    return parsed_values
