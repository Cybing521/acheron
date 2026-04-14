# Source Generated with Decompyle++
# File: tmpf2ekczbh.marshal (Python 3.11)

if self.unit_formatter:
    scaled_value = value * self.unit_formatter.conversion_scale + self.unit_formatter.conversion_offset
    return self.unit_formatter.format_bare(scaled_value)
return None(value)
