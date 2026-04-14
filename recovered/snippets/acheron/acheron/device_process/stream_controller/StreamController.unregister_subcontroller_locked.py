# Source Generated with Decompyle++
# File: tmpl8o1q8x1.marshal (Python 3.11)

if self.subcontroller == subcontroller:
    self.subcontroller = None
    self.radio_queue.put((StreamControl._REMOTE_CLOSED,))
    
    try:
        self.rgb_manager.remote_disconnected_locked()
        return None
    except Exception:
        return None
        return None

