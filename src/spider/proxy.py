import urllib.request
from lxml import etree
from src.spider.proxyCaches import getRandomIp

url = 'https://www.qidian.com/rank/hotsales'
# 浏览器伪装
# opener=urllib.request.build_opener()

# 设置代理
proxy = {'http': getRandomIp()}
proxy_support = urllib.request.ProxyHandler(proxy)
opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent',
                      'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
urllib.request.install_opener(opener)
html = urllib.request.urlopen(url).read().decode('utf-8')

# html=requests.get(url).text
# f = open('FC.html','w')
# f.write(str(html))
# f.close()
# print(html)

selector = etree.HTML(html)
info = selector.xpath('//div[@class="book-mid-info"]')

for each in info:
    name = each.xpath('h4/a[@data-eid="qd_C40"]/text()')
    author = each.xpath('p[@class="author"]/a[@class="name"]/text()')
    target = each.xpath('p[@class="author"]/a[@data-eid="qd_C42"]/text()')
    intro = each.xpath('p[@class="intro"]/text()')[0]
    print(name)
    print(author)
    print(target)
    print(intro + '\n')
