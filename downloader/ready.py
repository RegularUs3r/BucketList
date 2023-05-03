#!/usr/bin/env python3


import argparse


from downloader.start import *
from downloader.output import out
from downloader.evall import evaluation
from downloader.dicts import *



def xml():
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description="Created By: SickAndTired")
    parser.add_argument("-t", "--target", metavar="\b", required=True, help="Pay the rent!")
    parser.add_argument("-x", "--extensions", metavar="\b", help="Specify extensions separated by comma")
    parser.add_argument("-ch", "--cheader", metavar="\b", help="Specify a custom headers")
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("-x", "--proxy", metavar="\b", help="Proxy - http://IP:PORT")
    parser.add_argument(" ", nargs="*")
    args = parser.parse_args()
    target = args.target
    verbose = args.verbose
    extensions = args.extensions
    cheader = args.cheader
    proxy = args.proxy
    if verbose and target != "":
        start2(target, extensions, cheader, proxy)
    elif target != "":
        start(target, extensions, cheader, proxy)xtensions)

def cct_fuzz():
    print("Soon!")
