import re
import requests
import hashlib
import time
from concurrent.futures import ThreadPoolExecutor,as_completed

p = ThreadPoolExecutor(30)  # 创建一个进程池中，容纳线程个数30个

def get_index(url):
  respose = requests.get(url)
  if respose.status_code == 200:
    return respose.text


def parse_index(res):
  # res = res.result()  # 进程执行完毕后，得到1个对象
  urls = re.findall(r'class="items".*?href="(.*?)"', res, re.S)  # re.S 把文本信息转换成一行匹配

  for url in urls:
  #   # print(url)
    m_url = get_detail(url)
    p.submit(save, m_url)


def get_detail(url):
  if not url.startswith('http'):
    url = 'http://www.xiaohuar.com%s' % url
  result = requests.get(url)
  if result.status_code == 200:
    mp4_url_list = re.findall(r'id="media".*?src="(.*?)"', result.text, re.S)
    if mp4_url_list:
      print(mp4_url_list)
      mp4_url = mp4_url_list[0]
      print('detail %s' % mp4_url)
      return mp4_url
      # save(url)

def save(url):
  video = requests.get(url)
  if video.status_code == 200:
    m = hashlib.md5()
    m.update(url.encode('utf-8'))
    m.update(str(time.time()).encode('utf-8'))
    filename = r'%s.mp4' % m.hexdigest()
    filepath = r'c:\\java\mp4\%s' % filename
    with open(filepath, 'wb') as f:
      f.write(video.content)


def main():
  for i in range(5):
    index = get_index('http://www.xiaohuar.com/list-3-%s.html' % 1)
    parse_index(index)


if __name__ == '__main__':
  main()
