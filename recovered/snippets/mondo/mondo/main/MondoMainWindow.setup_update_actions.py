# Source Generated with Decompyle++
# File: tmp9a7r0ytg.marshal (Python 3.11)

is_frozen = getattr(sys, 'frozen', False)
valid_info = False
if is_frozen:
    main_dir = os.path.dirname(sys.executable)
    build_info_filename = os.path.join(main_dir, 'build_info.txt')
    
    try:
        f = open(build_info_filename, 'r', encoding = 'utf-8')
        lines = f.readlines()
        self.branch_name = lines[0].strip()
        self.commit_hash = lines[1].strip()
        self.build_key = lines[2].strip()
        valid_info = True
        
        try:
            None(None, None)
        with None:
            if not None:
                
                try:
                    
                    try:
                        pass
                    except Exception:
                        logger.exception('Could not read build_info.txt')

                    if not valid_info:
                        self.menuCheckForUpdates.setEnabled(False)
                        self.menuCheckForUpdates.setTitle(self.tr('Not Updatable'))
                        self.actionUpdateLatestStable.setEnabled(False)
                        self.actionUpdateCurrentBranch.setEnabled(False)
                        self.actionUpdateSpecificBranch.setEnabled(False)
                        self.actionUpdateSpecificCommit.setEnabled(False)
                        return None
                    if None.branch_name == 'master':
                        self.actionUpdateCurrentBranch.setEnabled(False)
                        self.actionUpdateCurrentBranch.setVisible(False)
                        return None
                    action_str = None.tr('Latest {}').format(self.branch_name)
                    self.actionUpdateCurrentBranch.setText(action_str)
                    return None



