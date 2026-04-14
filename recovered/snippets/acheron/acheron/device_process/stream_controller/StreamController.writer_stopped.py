# Source Generated with Decompyle++
# File: tmp45mh51x5.marshal (Python 3.11)

self.writer_lock
writer = self.writers.pop(schedule_id)
writer.close()
self.background_join_deque.append(writer)
self.logger.debug('Writer stopped for %s', schedule_id)
