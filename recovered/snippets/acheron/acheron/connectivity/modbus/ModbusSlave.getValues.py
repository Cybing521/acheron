# Source Generated with Decompyle++
# File: tmpxblsvy6f.marshal (Python 3.11)

read_address = address & -2
if read_address != address:
    word_count = (count + 2) // 2
else:
    word_count = (count + 1) // 2
results = []
for i in range(word_count):
    words = self.read_register_words(read_address + i * 2)
    results.extend(words)
    if address != read_address:
        results = results[1:]
results = results[:count]
return results[:count]
