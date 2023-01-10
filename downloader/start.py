#!/usr/bin/env python3


import xml.etree.ElementTree as ET
import urllib.request
import requests


from downloader.evall import evaluation
from downloader.output import out
from downloader.decoy import decoy
from downloader.futures import workers
from downloader.writers import download
from downloader.erroredones import erroredones


def start(target, extension):
    try:
        url = target
        if url[-1] != "/":
            url = target+"/"
            r = requests.get(url)
            root = ET.fromstring(r.content)
            evaluation(root, extension)
            decoy(url)
            erroredones(url)
        else:
            r = requests.get(url)
            root = ET.fromstring(r.content)
            evaluation(root, extension)
            decoy(url)
            erroredones(url)

    except MissingSchema:
        print("Invalid URL")


def start2(target, extension):
    try:
        url = target
        if url[-1] != "/":
            url = target+"/"
            r = requests.get(url)
            root = ET.fromstring(r.content)
            evaluation(root, extension)
            out()
            workers(url)
            erroredones(url)
        else:
            r = requests.get(url)
            root = ET.fromstring(r.content)
            evaluation(root, extension)
            out()
            workers(url)
            erroredones(url)

    except MissingSchema:
        print("Invalid URL")
