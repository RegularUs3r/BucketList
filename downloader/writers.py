#!/usr/bin/env python3


from progress.bar import Bar
import requests
import urllib3



from downloader.dicts import *



requests.urllib3.disable_warnings()
def download(url):
    print(" [+] Process started!")
    bar = Bar (f" [+] Files downloaded",max=sum(ext_counts.values()), fill="█")
    for items in bigdata:
        print("\r    Working on it", end=""),bar.next()
        fille = items
        filename = fille.replace("/", "")
        r = requests.get(url+fille, verify=False)
        if r.status_code != 200:
            failedones[fille] = failedones.get(fille, 0) + 1
        else:
            if filename[:1] == ".":
                f = open(f"files/{filename[1:]}", "wb")
                f.write(r.content)
                f.close()
            else:
                f = open(f"files/{filename}", "wb")
                f.write(r.content)
                f.close()
    bar.finish()
