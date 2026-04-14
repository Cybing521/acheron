# Source Generated with Decompyle++
# File: tmpj1539i_t.marshal (Python 3.11)

self.lock
if status == RFPowerStatus.NOT_SUPPORTED:
    del self.rf_power_statuses[controller]
else:
    except KeyError:
        pass
    except:
        self.rf_power_statuses[controller] = status
    None(None, None)
with None:
    if not None:
        pass
if not self.updating_rf:
    self._emit_rf_power_status()
    return None
