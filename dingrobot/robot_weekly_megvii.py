# its_time_to_book_dinner.py
# coding:utf-8
import requests
import json

dingtalk_url = "https://oapi.dingtalk.com/robot/send?access_token=xxx"

headers = {"Content-Type": "application/json; charset=utf-8"}

post_data = {
    "msgtype": "link", 
    "link": {
        "text": "该写周报啦，点我发周报",
       	"title": "该写周报啦", 
        "picUrl": "https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1031831432,3283603088&fm=26&gp=0.jpg", 
        "messageUrl": "xxx"
    },
    
    "at": {
        "isAtAll": True
    }
}

response = requests.post(dingtalk_url, data=json.dumps(post_data),headers=headers)
print(response.content)
