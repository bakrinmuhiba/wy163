import json
import os
import threading
import time

import requests
import re
import execjs
import execjs._runner_sources as _runner_sources

def get_validate(referer):
    # global ccc
    while 1:
        # opop=time.time()
        wy=Wy(referer)
        validate=wy.get_wy_v3_check()
        if(len(validate)>10):
            return validate

print(get_validate(""))
