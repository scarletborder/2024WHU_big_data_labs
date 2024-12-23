# 向env中得到的REGISTER_URL发送http请求

import requests
import time
import os

REGISTER_URI = os.getenv("REGISTER_URL", "")


def register(url):
    print("attempt to register " + url)
    response = requests.post(url + "/register", json={"url": "http://example-v2:8081"})
    print("resgister resp=" + response.text)


if __name__ == "__main__":
    if REGISTER_URI != "":
        register(REGISTER_URI)
        while True:
            time.sleep(2)
    else:
        print("no uri")
