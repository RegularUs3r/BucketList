#!/usr/bin/env python3

from downloader.dicts import *

def creator():
    for extension in alldict:
        for data in bigdata:
            if extension in data:
                data = {extension:[data]}
                ext_counts[extension] = ext_counts.get(extension, 0) + 1
