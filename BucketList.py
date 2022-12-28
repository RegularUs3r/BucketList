#!/usr/bin/env python3



import argparse, sys


from downloader.ready import *
from downloader.start import *



def initializer():
    try:
        arg = sys.argv[1]
        if arg == "xml":
            xml()
        elif arg == "spider-plus":
            spider_plus()
        elif arg != "xml" or arg != "spider-plus":
            print("No such modes!")
            print("Try no args for help")
    except IndexError:
        print("You should pick a mode")
        print(" │ ")
        print(" └──────[spider-plus]")
        print(" │ ")
        print(" └──────[xml]")


initializer()
