#!usr/bin/env python  #-*- coding:utf-8 _*-  """
"""
@file: robot_book_dinner.py 
@version:
@time: 2021/04/26 
@author: shuai
@function: 
"""
import requests
import json

dingtalk_url = "https://oapi.dingtalk.com/robot/send?access_token=xxx"

headers = {"Content-Type": "application/json; charset=utf-8"}

post_data = {
    "msgtype": "link",
    "link": {
        "text": "加班订餐啦！",
        "title": "订餐机器人提醒",
        "picUrl": "",
        "messageUrl": "https://www.meican.com"
    },

    "at": {
        "isAtAll": False
    }
}

response = requests.post(dingtalk_url, data=json.dumps(post_data), headers=headers)
print(response.content)
