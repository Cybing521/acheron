# Source Generated with Decompyle++
# File: tmpyy4ahf4i.marshal (Python 3.11)

alerts = (lambda .0: pass# WARNING: Decompyle incomplete
)(active_triggers())
without_alerts = (lambda .0: pass# WARNING: Decompyle incomplete
)(active_triggers())
if without_alerts != self.last_emitted_active_triggers:
    triggers_on = without_alerts.difference(self.last_emitted_active_triggers)
    triggers_off = self.last_emitted_active_triggers.difference(without_alerts)
    for trigger_name in sorted(triggers_on):
        self.logger.info('Trigger enabled: %s', trigger_name)
        for trigger_name in sorted(triggers_off):
            self.logger.info('Trigger disabled: %s', trigger_name)
            inactive = self.trigger_names.difference(without_alerts)
            self.active_triggers_changed.emit(self, without_alerts, inactive)
            self.last_emitted_active_triggers = without_alerts
            self.alerts_changed.emit(alerts)
            trigger_list = []
            for alert in alerts:
                trigger = self.alert_triggers.get(alert)
                if not trigger:
                    continue
                channel_info = self.channel_info.get(trigger.channel_id)
                if not channel_info:
                    continue
                subchannel_name = channel_info.subchannel_names[trigger.subchannel_index]
                trigger_list.append((trigger, subchannel_name))
                except IndexError:
                    continue
                if trigger_list:
                    self.dispatcher.alert_manager.send_alerts(self.logger, self.serial_number, self.display_name, trigger_list, self._email_callback)
                    return None
                return None
