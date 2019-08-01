import requests

r = requests.get('https://www.baidu.com/')
print(r.status_code)
# print(r.text)

r2 = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# print(r2.text)
print(r2.headers['Content-Type'])
# print(r2.cookies['ts'])
