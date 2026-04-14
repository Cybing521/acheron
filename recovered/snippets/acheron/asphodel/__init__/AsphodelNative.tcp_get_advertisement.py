# Source Generated with Decompyle++
# File: tmpiwj4ra88.marshal (Python 3.11)

adv_ptr = self.lib.asphodel_tcp_get_advertisement(device)
adv = adv_ptr.contents

def decode_safe(b):
    
    try:
        return b.decode('UTF-8')
    except UnicodeDecodeError:
        return 'ERROR'


return TCPAdvInfo(adv.tcp_version, bool(adv.connected), adv.max_incoming_param_length, adv.max_outgoing_param_length, adv.stream_packet_length, adv.protocol_type, decode_safe(adv.serial_number), adv.board_rev, decode_safe(adv.board_type), decode_safe(adv.build_info), decode_safe(adv.build_date), decode_safe(adv.user_tag1), decode_safe(adv.user_tag2), adv.remote_max_incoming_param_length, adv.remote_max_outgoing_param_length, adv.remote_stream_packet_length)
