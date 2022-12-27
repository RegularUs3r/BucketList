#!/usr/bin/env python3


import threading
import os


from downloader.writers import download
from downloader.dicts import * 



def workers(url):
    print(" [*] Do not exit 'til I'm done!")
    if os.path.exists("files"):
        os.system("rm -rf files")
        os.system("mkdir files")
    else:
        os.system("mkdir files")
    gethemall = threading.Thread(target=download, args=(url,))
    gethemall.start()
    gethemall.join()
