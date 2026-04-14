# Source Generated with Decompyle++
# File: tmp3vkvc2i5.marshal (Python 3.11)


try:
    f = open(trigger_filename, 'rt')
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

                ta.validate_json(contents) = TypeAdapter(list[DiskTrigger])
                trigger_dict = { }
                trigger_names = set()
                for t in triggers:
                    trigger_names.add(t.id)
                    trigger_set = trigger_dict.get(t.serial)
                    if not trigger_set:
                        trigger_set = set((t.convert(),))
                        trigger_dict[t.serial] = trigger_set
                        continue
                    trigger_set.add(t.convert())
                    return (trigger_dict, trigger_names)



