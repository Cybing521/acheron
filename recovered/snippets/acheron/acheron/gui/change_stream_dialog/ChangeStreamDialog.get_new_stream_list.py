# Source Generated with Decompyle++
# File: tmpw62ag_de.marshal (Python 3.11)

all_true = True
stream_list = []
for index in sorted(self.check_boxes.keys()):
    check_box = self.check_boxes[index]
    if check_box.isChecked():
        stream_list.append(index)
        continue
    all_true = False
    if all_true:
        return None
    return None
