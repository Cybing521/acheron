# Source Generated with Decompyle++
# File: tmpljagvfap.marshal (Python 3.11)

if self.channel_type < len(channel_type_names):
    s = channel_type_names[self.channel_type]
    channel_type_str = '{} ({})'.format(self.channel_type, s)
else:
    channel_type_str = '{}'.format(self.channel_type)
if self.unit_type < len(unit_type_names):
    s = unit_type_names[self.unit_type]
    unit_type_str = '{} ({})'.format(self.unit_type, s)
else:
    unit_type_str = '{}'.format(self.unit_type)
coefficients = self.coefficients[:self.coefficients_length]
chunk_lengths = self.chunk_lengths[:self.chunk_count]
chunks = []
for i, ptr in enumerate(self.chunks[:self.chunk_count]):
    length = chunk_lengths[i]
    chunk = bytes(ptr[:length])
    chunks.append(chunk)
    items = [
        ('name', self.name),
        ('name_length', self.name_length),
        ('channel_type', channel_type_str),
        ('unit_type', unit_type_str),
        ('filler_bits', self.filler_bits),
        ('data_bits', self.data_bits),
        ('samples', self.samples),
        ('bits_per_sample', self.bits_per_sample),
        ('minimum', self.minimum),
        ('maximum', self.maximum),
        ('resolution', self.resolution),
        ('coefficients', coefficients),
        ('coefficients_length', self.coefficients_length),
        ('chunks', chunks),
        ('chunk_lengths', chunk_lengths),
        ('chunk_count', self.chunk_count)]
    contents = (lambda .0: pass# WARNING: Decompyle incomplete
)(items())
    return '<AsphodelChannelInfo {' + contents + '}>'
