#!/usr/bin/env python3


import xml.etree.ElementTree as ET
import urllib.request
import requests
from requests.exceptions import MissingSchema

from downloader.evall import evaluation
from downloader.output import out
from downloader.decoy import decoy
from downloader.futures import workers
from downloader.writers import download
from downloader.erroredones import erroredones


def start(target, extension, header, proxy):
    try:
        url = target
        if url[-1] != "/":
            url = target+"/"
            r = requests.get(url)
            root = ET.fromstring(r.content)
            evaluation(root, extension)
            decoy(url, header, proxy)
            erroredones(url)
        else:
            r = requests.get(url)
            root = ET.fromstring(r.content)
            evaluation(root, extension)
            decoy(url, header, proxy)
            erroredones(url)

    except MissingSchema:
        print("Invalid URL")


def start2(target, extension, header, proxy):
    try:
        url = target
        if url[-1] != "/":
            url = target+"/"
            r = requests.get(url)
            root = ET.fromstring(r.content)
            evaluation(root, extension)
            out()
            workers(url, header, proxy)
            erroredones(url)
        else:
            r = requests.get(url)
            root = ET.fromstring(r.content)
            evaluation(root, extension)
            out()
            workers(url, header, proxy)
            erroredones(url)

    except MissingSchema:
        print("Invalid URL")
