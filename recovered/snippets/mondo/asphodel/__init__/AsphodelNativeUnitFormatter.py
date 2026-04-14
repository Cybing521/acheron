# Source Generated with Decompyle++
# File: tmps9px2e3m.marshal (Python 3.11)


def __init__(self, lib, formatter, recreate):
    self.lib = lib
    self.formatter = formatter
    self._recreate = recreate
    self.unit_ascii = self.formatter.unit_ascii.decode('ascii')
    self.unit_utf8 = self.formatter.unit_utf8.decode('UTF-8')
    self.unit_html = self.formatter.unit_html.decode('ascii')
    self.conversion_scale = self.formatter.conversion_scale
    self.conversion_offset = self.formatter.conversion_offset


def __del__(self):
    self.free()


def __reduce__(self):
    return self._recreate


def __eq__(self, other):
    if isinstance(other, self.__class__):
        self_tuple = (self.unit_ascii, self.unit_utf8, self.unit_html, self.conversion_scale, self.conversion_offset)
        other_tuple = (other.unit_ascii, other.unit_utf8, other.unit_html, other.conversion_scale, other.conversion_offset)
        return self_tuple == other_tuple


def free(self):
    if self.formatter:
        self.formatter.free(self.formatter)
        self.formatter = None
        return None


def format_bare(self, value):
    buffer = create_string_buffer(256)
    self.formatter.format_bare(self.formatter, buffer, len(buffer), value)
    return buffer.value.decode('ascii')


def format_ascii(self, value):
    buffer = create_string_buffer(256)
    self.formatter.format_ascii(self.formatter, buffer, len(buffer), value)
    return buffer.value.decode('ascii')


def format_utf8(self, value):
    buffer = create_string_buffer(256)
    self.formatter.format_utf8(self.formatter, buffer, len(buffer), value)
    return buffer.value.decode('UTF-8')


def format_html(self, value):
    buffer = create_string_buffer(256)
    self.formatter.format_html(self.formatter, buffer, len(buffer), value)
    return buffer.value.decode('ascii')

