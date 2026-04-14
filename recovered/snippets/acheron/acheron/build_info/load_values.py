# Source Generated with Decompyle++
# File: tmpe9zteyic.marshal (Python 3.11)

is_frozen = getattr(sys, 'frozen', False)
if is_frozen:
    main_dir = os.path.dirname(sys.executable)
    build_info_filename = os.path.join(main_dir, 'build_info.txt')
    
    try:
        f = open(build_info_filename, 'r', encoding = 'utf-8')
        lines = f.readlines()
        branch_name = lines[0].strip()
        commit_hash = lines[1].strip()
        build_key = lines[2].strip()
        build_date = lines[3].strip()
        
        try:
            None(None, None)
            return 
            with None:
                if not None, (branch_name, commit_hash, build_key, build_date):
                    
                    try:
                        
                        try:
                            pass
                        except Exception:
                            logger.exception('Could not read build_info.txt')

                        return None



