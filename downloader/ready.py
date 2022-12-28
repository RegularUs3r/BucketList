#!/usr/bin/env python3


import argparse


from downloader.start import *
from downloader.output import out
from downloader.evall import evaluation
from downloader.dicts import *



def xml():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", metavar="\b", required=True, help="target.com")
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("any", nargs="*")
    args = parser.parse_args()
    target = args.target
    verbose = args.verbose
    if verbose and target != "":
        start2(target)
    elif target != "":
        start(target)

def spider_plus():
    print("Soon!")
