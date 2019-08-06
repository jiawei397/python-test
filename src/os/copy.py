import os

dir_path = 'C:\Documents\图片\Camera Roll\image'
# print(os.listdir(dir_path))

# del_arr = []

for child_dir in os.listdir(dir_path):
  child_list = os.listdir(dir_path + '/' + child_dir)
  # print(child_list)
  if(len(child_list) == 1):
    # print(child_list)
    # print(child_dir)
    if(child_dir.endswith(')')):
      dir_name = child_dir.split('(')[0]
      # dir_name = child_dir[0:-4]
      # print(dir_name)
      base_dir = '../../tmp/' + dir_name
      if os.path.exists(base_dir) == False:
        os.makedirs(base_dir)
      del_dir = dir_path + '/' + child_dir
      os.link(del_dir + '/' + child_list[0], base_dir + '/' + child_list[0])
      # del_arr.append(del_dir)
      os.remove(del_dir + '/' + child_list[0])
      os.removedirs(del_dir)

# for dir in del_arr:
  # print(dir)
  # os.removedirs(dir)

# os.link('../resources/test.png', './a.png')
