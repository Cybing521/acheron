# Source Generated with Decompyle++
# File: tmpzs3amroi.marshal (Python 3.11)

self.controller.reset_lost_packets()
self.recentLostPackets.setText(str(0))
if self.recent_lost_packet_highlight:
    self.recent_lost_packet_highlight = False
    self.recentLostPackets.setStyleSheet('')
    return None
