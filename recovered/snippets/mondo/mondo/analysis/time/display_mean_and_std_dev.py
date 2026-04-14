# Source Generated with Decompyle++
# File: tmpnfn_0xld.marshal (Python 3.11)

value_strings = []
for x, y, name, unit in data:
    (mean, std_dev) = get_mean_std_dev_in_range(start_time, end_time, x, y)
    base_str = f'''mean={mean} {unit.utf8}, std dev={std_dev} {unit.utf8}'''
    if name:
        value_strings.append(f'''{name}: {base_str}''')
        continue
    value_strings.append(base_str)
    text = '\n'.join(value_strings)
    QtWidgets.QMessageBox.information(parent, title, text)
    return None
