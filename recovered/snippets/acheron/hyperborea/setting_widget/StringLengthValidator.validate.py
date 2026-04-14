# Source Generated with Decompyle++
# File: tmp6qpqvp9c.marshal (Python 3.11)


try:
    utf_bytes = input_text.encode('UTF-8')
except Exception:
    return 

if len(utf_bytes) <= self.max_length:
    return (QtGui.QValidator.State.Acceptable, input_text, pos)
return (None.QValidator.State.Invalid, input_text, pos)
