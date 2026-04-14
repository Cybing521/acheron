# Source Generated with Decompyle++
# File: tmpb4rwbfy5.marshal (Python 3.11)

index = self.graphChannelComboBox.currentIndex()
if index == -1:
    return None

try:
    return self.combo_box_channel_ids[index]
except IndexError:
    return None

