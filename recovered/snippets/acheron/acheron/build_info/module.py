# Source Generated with Decompyle++
# File: tmpj4emycmg.marshal (Python 3.11)

import functools
import logging
import os
import sys
from typing import Optional
logger = logging.getLogger(__name__)
_load_values = (lambda : is_frozen = getattr(sys, 'frozen', False)if is_frozen:
main_dir = os.path.dirname(sys.executable)build_info_filename = os.path.join(main_dir, 'build_info.txt')try:
f = open(build_info_filename, 'r', encoding = 'utf-8')lines = f.readlines()branch_name = lines[0].strip()commit_hash = lines[1].strip()build_key = lines[2].strip()build_date = lines[3].strip()try:
None(None, None)with None:
if not None, (branch_name, commit_hash, build_key, build_date):
try:
try:
passexcept Exception:
logger.exception('Could not read build_info.txt')None)()

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

