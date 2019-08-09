import requests

url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key='
# msg = {
#     "msgtype": "text",
#     "text": {
#         "content": "广州今日天气：29度，大部分多云，降雨概率：60%",
#         "mentioned_list": ["wangqing", "@all"],
#         "mentioned_mobile_list": ["13800001111", "@all"]
#     }
# }


def getMsg(content, list):
    # list.append('@all')
    mentioned_list = []
    if len(list) == 0:
        mentioned_list.append('@all')
    else:
        for i in list:
            mentioned_list.append('@' + i)

    return {
        "msgtype": "text",
        "text": {
            "content": content,
            "mentioned_list": mentioned_list
            # "mentioned_mobile_list": ["13800001111", "@all"]
        }
    }


def post(key, content, list):
    msg = getMsg(content=content, list=list)
    requests.post(url + key, json=msg)


if __name__ == '__main__':
    content = input('发布消息：')
    list = input('联系人：')
    if len(list) > 0:
        list = list.split(',')
    else:
        list = []
    post('eefb5ba8-77f3-4538-8030-bfa52bb661f2', content, list)
