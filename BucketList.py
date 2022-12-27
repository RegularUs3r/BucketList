#!/usr/bin/env python3



import argparse
from downloader.start import *
from downloader.output import out
from downloader.evall import evaluation
from downloader.dicts import *


parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(description="Created By: SickAndTired")
parser.add_argument("-m", "--mode", metavar="\b", required=True, help="XML, DORK, BUZZ")
parser.add_argument("-t", "--target", metavar="\b", required=True, help="target.com")
parser.add_argument("-v", "--verbose", action="store_true", help="Displays quatity of files")

args = parser.parse_args()
mode = args.mode
target = args.target
verbose = args.verbose

def vai_teia():
    if verbose and mode == "XML" and target != "":
        start2(target)
    elif mode == "XML" and target != "":
        start(target)

vai_teia()
