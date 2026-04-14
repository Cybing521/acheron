# Source Generated with Decompyle++
# File: tmpant0yd4p.marshal (Python 3.11)

if self.suffix():
    remove_suffix = input_text.endswith(self.suffix())
    if remove_suffix:
        s = input_text.rsplit(self.suffix(), 1)[0]
    else:
        s = input_text
else:
    remove_suffix = False
    s = input_text
ret = self.validator.validate(s, pos)
if remove_suffix:
    return (ret[0], ret[1] + self.suffix(), ret[2])
