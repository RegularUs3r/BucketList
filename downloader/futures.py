#!/usr/bin/env python3



import concurrent.futures
import os



from downloader.writers import download
from downloader.dicts import * 



def workers(url, header, proxy):
    print(" [*] Do not exit 'til I'm done!")
    if os.path.exists("files"):
        os.system("rm -rf files")
        os.system("mkdir files")
    else:
        os.system("mkdir files")
    with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
        fdown = executor.submit(download, url, header, proxy)
