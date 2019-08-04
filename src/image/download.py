import os

dir = '../../tmp/image'
os.makedirs(dir, exist_ok=True)
IMAGE_URL = "http://g.hiphotos.baidu.com/image/pic/item/5366d0160924ab18014cefd83bfae6cd7a890b82.jpg"


def urllib_download():
  from urllib.request import urlretrieve
  urlretrieve(IMAGE_URL, '%s/img1.png' % dir)


def request_download():
  import requests
  r = requests.get(IMAGE_URL)
  with open('%s/img2.png' % dir, 'wb') as f:
    f.write(r.content)


def chunk_download():
  import requests
  r = requests.get(IMAGE_URL, stream=True)
  with open('%s/img3.png' % dir, 'wb') as f:
    for chunk in r.iter_content(chunk_size=32):
      f.write(chunk)


urllib_download()
print('download img1')
request_download()
print('download img2')
chunk_download()
