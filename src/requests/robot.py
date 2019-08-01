import requests

url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=eefb5ba8-77f3-4538-8030-bfa52bb661f2'
msg = {
    "msgtype": "text",
    "text": {
        "content": "广州今日天气：29度，大部分多云，降雨概率：60%",
        "mentioned_list":["wangqing","@all"],
        "mentioned_mobile_list":["13800001111","@all"]
    }
}

requests.post(url, json=msg)
