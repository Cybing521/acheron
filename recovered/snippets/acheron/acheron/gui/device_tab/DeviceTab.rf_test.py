# Source Generated with Decompyle++
# File: tmpzh2wm50a.marshal (Python 3.11)

dialog = RFTestDialog(self)

try:
    ret = dialog.exec()
    if ret == 0:
        dialog.deleteLater()
        return None
    test_params = None.get_test_params()
    dialog.deleteLater()
except:
    dialog.deleteLater()

(finished_rx_pipe, finished_tx_pipe) = multiprocessing.Pipe(False)
params = RFTestParams(test_params, cast(multiprocessing.connection.Connection, finished_rx_pipe))
self.controller.start_rf_test(params)
msg_box = QtWidgets.QMessageBox(self)
msg_box.setWindowTitle(self.tr('RF Test'))
msg_box.setText(self.tr('Running RF Test'))
msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Abort)
button = msg_box.button(QtWidgets.QMessageBox.StandardButton.Abort)
button.setText(self.tr('Stop'))
self.controller.rf_test_finished.connect(msg_box.reject)
msg_box.exec()
finished_tx_pipe.send(None)
