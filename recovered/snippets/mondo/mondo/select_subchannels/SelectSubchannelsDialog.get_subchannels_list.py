# Source Generated with Decompyle++
# File: tmpwg1dlzbk.marshal (Python 3.11)

selected_subchannels = []
for index_tuple in sorted(self.subchannel_buttons.keys()):
    check_box = self.subchannel_buttons[index_tuple]
    if check_box.isChecked():
        selected_subchannels.append(index_tuple)
    return selected_subchannels
