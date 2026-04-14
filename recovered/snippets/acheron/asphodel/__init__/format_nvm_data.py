# Source Generated with Decompyle++
# File: tmpege44zq6.marshal (Python 3.11)


def to_ascii(c):
    c = chr(c)
    if c in string.whitespace:
        return ' '
    if None in string.printable:
        return c

output = []
for i in range(0, len(data), size):
    data_chunk = data[i:min(len(data), i + size)]
    hex_values = ' '.join(map('{:02x}'.format, data_chunk))
    filler = '   ' * (size - len(data_chunk))
    ascii_values = ''.join(map(to_ascii, data_chunk))
    output.append(hex_values + filler + ' ' + ascii_values)
    return output
