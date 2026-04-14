# Source Generated with Decompyle++
# File: tmp7g_n5vnf.marshal (Python 3.11)

if not self.hw_tests:
    return None
None.logger.info('Running Hardware Tests')
(hw_test_funcs, run_id) = self.hw_tests

try:
    self.device_lock
    for hw_test_func, test_id in hw_test_funcs:
        data = hw_test_func(self.device)
        self.status_pipe_lock
        self.status_pipe.send((StreamStatus.HARDWARE_TEST_FUNCTION_FINISHED, run_id, test_id, data))
        None(None, None)
    with None:
        if not None:
            pass
    continue
    except Exception:
        self.logger.exception('Failure in HW test')
        continue
    
    try:
        None(None, None)
    with None:
        if not None:
            
            try:
                
                try:
                    self.hw_tests = None
                    self.status_pipe_lock
                    self.status_pipe.send((StreamStatus.HARDWARE_TEST_RUN_FINISHED, run_id))
                    None(None, None)
                with None:
                    if not None:
                        pass

                self.logger.info('Finished Hardware Tests')
                return None
            except:
                self.hw_tests = None
                self.status_pipe_lock
                self.status_pipe.send((StreamStatus.HARDWARE_TEST_RUN_FINISHED, run_id))
                None(None, None)
            except:
                with None:
                    if not None:
                        pass

            self.logger.info('Finished Hardware Tests')


