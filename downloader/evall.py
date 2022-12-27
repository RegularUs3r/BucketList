#!/usr/bin/env python3



import xml.etree.ElementTree as ET



from downloader.dicts import *
from downloader.creator import creator



def evaluation(root):
    for child in root.iter("*"):
        if "Key" in child.tag:
            data = child.text
            if "/" in data and "." in data:
                bigdata.append(data)
                ext = "." + data.split(".")[-1]
                if ext not in alldict:
                    alldict.append(ext)
    creator()
