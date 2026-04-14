# Source Generated with Decompyle++
# File: tmpin27_mgg.marshal (Python 3.11)

import logging
import re
from typing import Any
import requests
logger = logging.getLogger(__name__)

def log_event(serial = None, category = None, description = None, **kwargs):
    sn_filtered = re.sub('[^\\d]', '', serial)
    
    try:
        sn_int = int(sn_filtered)
    except Exception:
        raise ValueError('Non-numeric serial number')

    data = kwargs.copy()
    data['serialNumber'] = sn_int
    data['category'] = str(category)
    data['description'] = str(description)
    url = 'https://api.suprocktech.com/events/create'
    response = requests.post(url, json = data)
    response.raise_for_status()

