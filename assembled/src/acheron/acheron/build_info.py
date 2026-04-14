# Source Generated with Decompyle++
# File: build_info.pyc (Python 3.11)

import functools
import logging
import os
import sys
from typing import Optional
logger = logging.getLogger(__name__)
# INVALID FROM DECOMPILER: _load_values = (lambda : is_frozen = getattr(sys, 'frozen', False)if is_frozen:
# INVALID FROM DECOMPILER: main_dir = os.path.dirname(sys.executable)build_info_filename = os.path.join(main_dir, 'build_info.txt')try:
# INVALID FROM DECOMPILER: f = open(build_info_filename, 'r', encoding = 'utf-8')lines = f.readlines()branch_name = lines[0].strip()commit_hash = lines[1].strip()build_key = lines[2].strip()build_date = lines[3].strip()try:
# INVALID FROM DECOMPILER: None(None, None)with None:
# INVALID FROM DECOMPILER: if not None, (branch_name, commit_hash, build_key, build_date):
# INVALID FROM DECOMPILER: try:
# INVALID FROM DECOMPILER: try:
# INVALID FROM DECOMPILER: passexcept Exception:
# INVALID FROM DECOMPILER: logger.exception('Could not read build_info.txt')None)()

# NOTE: assembled from module-level decompilation plus snippet/disassembly fallbacks.
# NOTE: function defaults and some class-level assignments may need manual repair.

def _load_values():
    is_frozen = getattr(sys, 'frozen', False)
    if not is_frozen:
        return None
    main_dir = os.path.dirname(sys.executable)
    build_info_filename = os.path.join(main_dir, 'build_info.txt')
    try:
        with open(build_info_filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        branch_name = lines[0].strip()
        commit_hash = lines[1].strip()
        build_key = lines[2].strip()
        build_date = lines[3].strip()
        return (branch_name, commit_hash, build_key, build_date)
    except Exception:
        logger.exception('Could not read build_info.txt')
        return None

def get_branch_name():
    values = _load_values()
    if values:
        return values[0]

def get_commit_hash():
    values = _load_values()
    if values:
        return values[1]

def get_build_key():
    values = _load_values()
    if values:
        return values[2]

def get_build_date():
    values = _load_values()
    if values:
        return values[3]
