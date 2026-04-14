# Source Generated with Decompyle++
# File: tmpi6kvqo8b.marshal (Python 3.11)

for schedule_list in schedule_items.values():
    for schedule_item in schedule_list:
        if schedule_item.trigger and schedule_item.trigger not in trigger_names:
            logger.warning('Unknown trigger name %s', schedule_item.trigger)
        return None
