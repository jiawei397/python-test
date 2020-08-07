# -*- coding: utf-8 -*-
import urllib.request
import json
import requests
import os

path = 'D:\\图片\\images'

# id = '5829543885'
id = '6048132583'
proxy_addr = "113.195.17.123:9999"
pic_num = 0
weibo_name = "" #微博昵称


def use_proxy(url, proxy_addr):
    req = urllib.request.Request(url)
    req.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
    req.add_header("Cookie", "SINAGLOBAL=5097567953065.36.1579164672880; UOR=,,www.baidu.com; _s_tentry=www.baidu.com; Apache=8901459481958.242.1596768986311; ULV=1596768986385:8:1:1:8901459481958.242.1596768986311:1594952661344; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWRyIuLQ5W9j37q-IAzQrUq5JpX5KzhUgL.FozpSKBcSK-7eK22dJLoIpjLxKMLB.2LB-2LxKnLB.BLB.zLxKqL1KnL1h5t; SUHB=0z1x_EyLvPJV-8; ALF=1628305345; SSOLoginState=1596769346; TC-V5-G0=799b73639653e51a6d82fb007f218b2f; wb_view_log_2154655011=1536*8641.25; TC-Page-G0=62b98c0fc3e291bc0c7511933c1b13ad|1596769426|1596769366; webim_unReadCount=%7B%22time%22%3A1596769575269%2C%22dm_pub_total%22%3A3%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A2%7D")

    proxy = urllib.request.ProxyHandler({'http': proxy_addr})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
    return data


def get_containerid(url):
    data = use_proxy(url, proxy_addr)
    content = json.loads(data).get('data')
    for data in content.get('tabsInfo').get('tabs'):
        if (data.get('tab_type') == 'weibo'):
            containerid = data.get('containerid')
    return containerid


def get_userInfo(id):
    url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=' + id
    data = use_proxy(url, proxy_addr)
    content = json.loads(data).get('data')
    profile_image_url = content.get('userInfo').get('profile_image_url')
    description = content.get('userInfo').get('description')
    profile_url = content.get('userInfo').get('profile_url')
    verified = content.get('userInfo').get('verified')
    guanzhu = content.get('userInfo').get('follow_count')
    global weibo_name
    weibo_name = content.get('userInfo').get('screen_name')
    fensi = content.get('userInfo').get('followers_count')
    gender = content.get('userInfo').get('gender')
    urank = content.get('userInfo').get('urank')
    print("微博昵称：" + weibo_name + "\n" + "微博主页地址：" + profile_url + "\n" + "微博头像地址：" + profile_image_url + "\n" + "是否认证：" + str(
        verified) + "\n" + "微博说明：" + description + "\n" + "关注人数：" + str(guanzhu) + "\n" + "粉丝数：" + str(
        fensi) + "\n" + "性别：" + gender + "\n" + "微博等级：" + str(urank) + "\n")


def get_weibo(id):
    global pic_num
    i = 200
    while True:
        url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=' + id
        weibo_url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=' + id + '&containerid=' + get_containerid(
            url) + '&page=' + str(i)
        try:
            data = use_proxy(weibo_url, proxy_addr)
            content = json.loads(data).get('data')
            cards = content.get('cards')
            if (len(cards) > 0):
                for j in range(len(cards)):
                    print(weibo_name + "-----正在爬取第" + str(i) + "页，第" + str(j) + "条微博------")
                    card_type = cards[j].get('card_type')
                    if (card_type == 9):
                        mblog = cards[j].get('mblog')
                        if mblog.get('pics') != None:
                            pic_archive = mblog.get('pics')
                            for _ in range(len(pic_archive)):
                                pic_num += 1
                                print(pic_archive[_]['large']['url'])
                                imgurl = pic_archive[_]['large']['url']
                                img = requests.get(imgurl)
                                imgName = imgurl.split("/")[-1:][0]
                                f = open(path + '\\' + weibo_name + '\\' + weibo_name + '_' + imgName,
                                         'ab')  # 存储图片，多媒体文件需要参数b（二进制文件）
                                f.write(img.content)  # 多媒体存储content
                                f.close()

                i += 1
            else:
                break
        except Exception as e:
            print(e)
            pass


if __name__ == "__main__":
    get_userInfo(id)
    if os.path.isdir(path + "\\" + weibo_name):
        pass
    else:
        os.makedirs(path + "\\" + weibo_name) #循环创建
    get_weibo(id)
