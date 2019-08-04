import re
import requests

res = requests.get('http://www.xiaohuar.com/v/')
# print(res.text)

urls = re.findall(r'class="items".*?href="(.*?)"', res.text, re.S)
# print(urls)

url = urls[5]
result = requests.get(url)

mp4_url = re.findall(r'id="media".*?src="(.*?)"', result.text, re.S)[0]

video = requests.get(mp4_url)

with open('d:\\a.mp4', 'wb') as f:
  f.write(video.content)
