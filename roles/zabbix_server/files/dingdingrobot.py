#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json
import sys
import os
 
headers = {'Content-Type': 'application/json;charset=utf-8'}
api_url = "" #dingding token
 
def msg(text):
    json_text= {
     "msgtype": "text",
        "at": {
            "atMobiles": [
                "13153669XXX"
            ],
            "isAtAll": False
        },
        "text": {
            "content": text
        }
    }
    print requests.post(api_url,json.dumps(json_text),headers=headers).content
     
if __name__ == '__main__':
    text = sys.argv[1]
    msg(text)