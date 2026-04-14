# Source Generated with Decompyle++
# File: tmpiahsr9tq.marshal (Python 3.11)

rf_power_needed = (lambda .0: pass# WARNING: Decompyle incomplete
)(schedule_items())
schedule_ids_set = set()
for schedule_item in schedule_items:
    schedule_ids_set.add(schedule_item.id)
    if schedule_item.output_config:
        writer = StreamWriter(self.logger, device_info, extra_info, schedule_item, self.settings.default_output_config, self)
        self.writer_lock
        self.writers[schedule_item.id] = writer
        None(None, None)
    else:
        with None:
            if not any:
                pass
    self.status_pipe_lock
    self.status_pipe.send((StreamStatus.ONGOING_ITEMS, schedule_ids_set, rf_power_needed, len(self.schedule)))
    None(None, None)
    return None
    with None:
        if not None:
            pass
