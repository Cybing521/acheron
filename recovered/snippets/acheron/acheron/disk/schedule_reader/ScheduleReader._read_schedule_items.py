# Source Generated with Decompyle++
# File: tmptjnt6n44.marshal (Python 3.11)


try:
    f = open(schedule_filename, 'rt')
    contents = f.read()
    
    try:
        None(None, None)
    with None:
        if not None:
            
            try:
                
                try:
                    pass
                except FileNotFoundError:
                    return 

                ta.validate_json(contents) = TypeAdapter(list[DiskSchedule])
                now = datetime.now(timezone.utc)
                single_schedule = { }
                cron_schedule = { }
                all_serials = set()
                for schedule_item in schedule_items:
                    if schedule_item.start_time and now > schedule_item.start_time:
                        continue
                    all_serials.add(schedule_item.serial)
                    serial = schedule_item.get_base_serial()
                    if schedule_item.is_single_item():
                        schedule_list = single_schedule.setdefault(serial, [])
                    else:
                        schedule_list = cron_schedule.setdefault(serial, [])
                    schedule_list.append(schedule_item)
                    return (single_schedule, cron_schedule, all_serials)



