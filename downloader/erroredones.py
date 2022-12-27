#!/usr/bin/env python3


from downloader.dicts import *
from downloader.retry import retry

def erroredones(url):
    print(" [-] Checking for failed files")
    if sum(failedones.values()) > 0:
        retry(url)
    else:
        pass
