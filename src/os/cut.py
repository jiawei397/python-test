import os


def shear_dile(src, dst):
    if os.path.isdir(src):
        if not os.listdir(src):
            os.rmdir(src)
            print('移除空目录: ' + src)
        else:
            for d in os.listdir(src):
                shear_dile(os.path.join(src, d), dst)
    if os.path.isfile(src):
        print("文件剪切:", src)
        fn = os.path.basename(src)
        if not os.path.exists(dst + './' + fn):
            os.rename(src, dst + './' + fn)


shear_dile("H:\\手机图片", "D:\\华为手机")
