# Source Generated with Decompyle++
# File: tmph8puym_x.marshal (Python 3.11)

for channel_id, fields in self.subchannel_fields.items():
    for mean_field, std_dev_field in enumerate(fields):
        for limit_type in (LimitType.MEAN_HIGH_LIMIT, LimitType.MEAN_LOW_LIMIT):
            id = f'''_alert_{channel_id}_{i}_{limit_type}'''
            if id in alerts:
                mean_field.set_alert(True)
            
            mean_field.set_alert(False)
            for limit_type in (LimitType.STD_HIGH_LIMIT, LimitType.STD_LOW_LIMIT):
                id = f'''_alert_{channel_id}_{i}_{limit_type}'''
                if id in alerts:
                    std_dev_field.set_alert(True)
                
                std_dev_field.set_alert(False)
                return None
