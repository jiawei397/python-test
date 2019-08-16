import os

# dir_path = 'C:\Documents\图片\Camera Roll\image'
dir_path = '../'
# print(os.listdir(dir_path))

# del_arr = []

for child_dir in os.listdir(dir_path):
  child_dir_path = os.path.join(dir_path, child_dir)
  if os.path.isdir(child_dir_path):
      size = os.path.getsize(child_dir_path)
      if size > 0:
        print(child_dir_path + ': ' + str(size))
