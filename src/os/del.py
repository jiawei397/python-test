import os

def delEmptyDir(dir):
  if os.path.isdir(dir):
    child_list = os.listdir(dir)
    if len(child_list) == 0:
      os.removedirs(dir)
    else:
      for child_dir in child_list:
        delEmptyDir(dir + '/' + child_dir)



if __name__ == '__main__':
  delEmptyDir('../../tmp')
