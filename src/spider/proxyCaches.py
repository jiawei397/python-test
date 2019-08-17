import urllib.request
from lxml import etree
import random

url = 'https://www.xicidaili.com/nn/'
# 浏览器伪装
# opener=urllib.request.build_opener()

# 设置代理
proxy = {'http': '120.83.110.50:9999'}
proxy_support = urllib.request.ProxyHandler(proxy)
opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent',
                      'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'),('Host','tieba.baidu.com')]
urllib.request.install_opener(opener)
html = urllib.request.urlopen(url).read().decode('utf-8')

# html=requests.get(url).text
# f = open('FC.html','w')
# f.write(str(html))
# f.close()
# print(html)

selector = etree.HTML(html)
info = selector.xpath('//tr[@class="odd"]')

def getIPs():
    ips = []
    for each in info:
        arr = each.xpath('td/text()')
        # print(arr[0] + ':' + arr[1])
        ip = arr[0] + ':' + arr[1]
        ips.append(ip)
        # name = each.xpath('h4/a[@data-eid="qd_C40"]/text()')
        # author = each.xpath('p[@class="author"]/a[@class="name"]/text()')
        # target = each.xpath('p[@class="author"]/a[@data-eid="qd_C42"]/text()')
        # intro = each.xpath('p[@class="intro"]/text()')[0]
        # print(name)
        # print(author)
        # print(target)
        # print(intro + '\n')
    return ips

def getRandomIp():
    ips = getIPs()
    ip = random.choice(ips)
    # print(ip)
    return ip

if __name__ == '__main__':
    ip = getRandomIp()
    print(ip)
