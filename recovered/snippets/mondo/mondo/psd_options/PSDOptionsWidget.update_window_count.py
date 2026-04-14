# Source Generated with Decompyle++
# File: tmpl4lz3j3j.marshal (Python 3.11)

window_counts = []
for chunks in self.chunks_list:
    window_count = 0
    for chunk in chunks:
        chunk_size = len(chunk[0])
        window_count += 1 + (chunk_size - window_size) // (window_size - overlap_points)
        window_counts.append(window_count)
        s = (lambda .0: pass# WARNING: Decompyle incomplete
)(window_counts())
        self.windowCount.setText(s)
        return None
