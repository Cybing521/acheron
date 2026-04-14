# Source Generated with Decompyle++
# File: tmpwwf2sw55.marshal (Python 3.11)

children = []
self.lock
for c in self.controllers.values():
    if c.parent_controller == controller:
        children.append(c)
    None(None, None)
with None:
    if not None:
        pass
for child in children:
    self.stop_controller(child)
    controller.stop()
    last_power_needed = False
    self.lock
    serial_number_tuples = set()
    for serial_numbers, c in self.controllers.items():
        if c == controller:
            serial_number_tuples.add(serial_numbers)
        for serial_numbers in serial_number_tuples:
            del self.controllers[serial_numbers]
            del self.controller_info[controller]
        except KeyError:
            pass
        del self.rf_power_statuses[controller]
    except KeyError:
        pass
    if self.rf_power_needed:
        self.rf_power_needed.discard(controller)
        if not self.rf_power_needed:
            last_power_needed = True
self.disconnected_controllers.discard(controller)
None(None, None)
