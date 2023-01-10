#!/usr/bin/env python3


import argparse


from downloader.start import *
from downloader.output import out
from downloader.evall import evaluation
from downloader.dicts import *



def xml():
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description="Created By: SickAndTired")
    parser.add_argument("-t", "--target", metavar="\b", required=True, help="some-target-bucket.s3-sa-east-1.amazonaws.com")
    parser.add_argument("-x", "--extensions", metavar="\b", help="specify extensions separated by comma")
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument(" ", nargs="*")
    args = parser.parse_args()
    target = args.target
    verbose = args.verbose
    extensions = args.extensions.split(",")
    if verbose and target != "":
        start2(target, extensions)
    elif target != "":
        start(target, extensions)

def cct_fuzz():
    print("Soon!")
