#!/usr/bin/env python3



import requests
import urllib3



from downloader.dicts import *



requests.urllib3.disable_warnings()
def retry(url):
    slash = "/"
    for items in failedones:
        filename = items.replace("/", "")
        r = requests.get(url+items, verify=False)
        if r.status_code == 403 and "xml version" in r.text:
            print(f" [{r.status_code}] - [{items}]")
        elif items[:2] == "//":
            file = items[2:]
            r = requests.get(url+file, verify=False)
            f= open(f"files/{filename}", "wb")
            f.write(r.content)
            f.close()
        elif items[:1] == ".":
            r = requests.get(url+file, verify=False)
            if r.status_code == 200:
                f= open(f"files/{filename}", "wb")
                f.write(r.content)
                f.close()
            else:
                file = items[1:]
                r = requests.get(url+file, verify=False)
                f= open(f"files/{filename}", "wb")
                f.write(r.content)
                f.close()
        else:
            print(f" *[{r.status_code}]* - [{items}]")
