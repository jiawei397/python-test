import os

def delDir(dir, isDelFile):
  if os.path.isdir(dir):
    child_list = os.listdir(dir)
    if len(child_list) == 0:
      os.removedirs(dir)
    else:
      for child_dir in child_list:
        delDir(dir + '/' + child_dir)
  else:
    if isDelFile:
        os.remove(dir)



if __name__ == '__main__':
  delDir('C:\\Documents\\图片\\Camera Roll')
