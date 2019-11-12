from PIL import Image
import os


origin_path = '../../tmp/'

def save(imgName):
    im = Image.open(os.path.join('../../tmp/', imgName))
    name = os.path.splitext(imgName)[0] + '.jpg'
    im.save(os.path.join('../../jpg/', name), 'jpeg')

for img in os.listdir(origin_path):
    print(img)
    # print(os.path.splitext(img))
    # print(os.path.abspath(img))
    # name = os.path.splitext(img)[0]
    save(img)
