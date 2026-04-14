# Source Generated with Decompyle++
# File: tmps1o2l5t3.marshal (Python 3.11)

dialog = SelectSynchronousDialog(header['streams'], header['channels'], parent = parent)
ret = dialog.exec()
if ret == 0:
    return None
channel_list = None.get_channel_list()
if len(channel_list) == 0:
    return None
