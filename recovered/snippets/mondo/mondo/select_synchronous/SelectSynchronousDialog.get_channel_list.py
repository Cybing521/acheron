# Source Generated with Decompyle++
# File: tmplv9neckn.marshal (Python 3.11)

for i, stream_button in enumerate(self.stream_buttons):
    if stream_button.isChecked():
        indexes = set()
        for ch_index, check_box in self.channel_groups[i].items():
            if check_box.isChecked():
                indexes.add(ch_index)
            
            return None, sorted(indexes)
            return []
