#!/usr/bin/env python3


import argparse


from downloader.start import *
from downloader.output import out
from downloader.evall import evaluation
from downloader.dicts import *



def xml():
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description="Created By: SickAndTired")
    parser.add_argument("-t", "--target", metavar="", required=True, help="Pay the rent!")
    parser.add_argument("-e", "--extensions", metavar="", help="Specify extensions separated by comma")
    parser.add_argument("-H", "--header", metavar="", help="Specify a custom header")
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("-x", "--proxy", metavar="", help="Proxy - http://IP:PORT")
    parser.add_argument(" ", nargs="*")
    args = parser.parse_args()
    target = args.target
    verbose = args.verbose
    extensions = args.extensions
    header = args.header
    proxy = args.proxy
    if verbose and target != "":
        start2(target, extensions, proxy, header)
    elif target != "":
        start(target, extensions, proxy, header)

def cct_fuzz():
    print("Soon!")
