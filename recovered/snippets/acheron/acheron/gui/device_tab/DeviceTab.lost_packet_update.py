# Source Generated with Decompyle++
# File: tmphypcfoxi.marshal (Python 3.11)

self.lost_packet_count = total
self.lost_packet_last_time = last_datetime
self.recentLostPackets.setText(str(recent))
if recent > 0:
    if not self.recent_lost_packet_highlight:
        self.recent_lost_packet_highlight = True
        self.recentLostPackets.setStyleSheet('* { color: black; background-color: red }')
        return None
    return None
if None.recent_lost_packet_highlight:
    self.recent_lost_packet_highlight = False
    self.recentLostPackets.setStyleSheet('')
    return None
