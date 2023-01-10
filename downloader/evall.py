#!/usr/bin/env python3



import xml.etree.ElementTree as ET



from downloader.dicts import *
from downloader.creator import creator



def evaluation(root, extensions):
    for child in root.iter("*"):
        if "Key" in child.tag and "." in child.text:
            data = child.text
            if extensions == None:
                #print(data)
                bigdata.append(data)
                ext = "." + data.split(".")[-1]
                if ext not in alldict:
                    alldict.append(ext)
            elif data.split(".")[-1] in extensions:
                bigdata.append(data)
                ext = "." + data.split(".")[-1]
                if ext not in alldict:
                    alldict.append(ext)
    creator()
