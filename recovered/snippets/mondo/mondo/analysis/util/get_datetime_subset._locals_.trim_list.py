# Source Generated with Decompyle++
# File: tmpctdhek3a.marshal (Python 3.11)

new_lost_packet_list = []
for last, current, index in lost_packet_list:
    if index > start_index and index < end_index:
        new_lost_packet_list.append((last, current, index - start_index))
    return new_lost_packet_list
