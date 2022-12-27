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


def start(target):
    url = target
    r = requests.get(url)
    root = ET.fromstring(r.content)
    evaluation(root)
    decoy(url)
    erroredones(url)


def start2(target):
    url = target
    r = requests.get(url)
    root = ET.fromstring(r.content)
    evaluation(root)
    out()
    workers(url)
    erroredones(url)
