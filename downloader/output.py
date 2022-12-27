#!/usr/bin/env python3



from downloader.dicts import *
from downloader.futures import workers



def out():
    for x, values in zip(alldict, ext_counts.values()):
        ext = x.split(".")[-1]
        print(f" {ext.upper()} Files - {values}")
