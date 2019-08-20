import os


def rename_func(path):
    for file in os.listdir(path):
        fileName = os.path.splitext(file)[0]
        # print(fileName)
        fileNew = fileName[-10:] + os.path.splitext(file)[1]
        # print(fileNew)
        # fileNew = file + '.jpg'
        # print("Old:", file, "New", fileNew)
        if (fileNew != file and len(fileName) > 20):
            if (not os.path.exists(path + fileNew)):
                os.rename(path + file, path + fileNew)
            else:
                print(file)


path = 'C:\\Documents\\wk\\gitee\\chromeTest\\tmp\\许允美\\'

rename_func(path)
