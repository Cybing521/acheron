# Source Generated with Decompyle++
# File: tmp094nrpmk.marshal (Python 3.11)

message = self.format(record)

try:
    serial_number = record.serial_number
    
    try:
        model = _models[serial_number]
        
        try:
            pass
        except KeyError:
            model = GUILogModel(_global_deque)
            _models[serial_number] = model
            
            try:
                pass
            try:
                model.log_message(message)
                return None
            except AttributeError:
                _global_deque.append(message)
                for model in _models.values():
                    model.log_message(message)
                    return None




