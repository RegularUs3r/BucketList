#!/usr/bin/env python3


from downloader.dicts import *
from downloader.futures import workers
from downloader.writers import download



def decoy(url, proxy, header):
    workers(url, proxy, header)
