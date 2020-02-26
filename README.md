## python ##

### 常用命令 ###

  python -m -pip install XX

使用pip的时候在后面加上-i参数，指定pip的下载源

  pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple

上面命令每次运行需要指定网址，可进行永久修改：

windows下: 在user目录中创建一个pip目录，如：C:\Users（用户）\xx\pip，新建文件pip.ini，内容如下

  [global]
  index-url = https://pypi.tuna.tsinghua.edu.cn/simple

linux下: 修改 ~/.pip/pip.conf （如果没有自己创建一个）， 内容如下：

  [global]
  index-url = https://pypi.tuna.tsinghua.edu.cn/simple

参考：https://blog.csdn.net/yamadeee/article/details/80178996

打包命令：
pyinstaller -F app.py

### window安装包失败

到这个网站下载失败的包：https://www.lfd.uci.edu/~gohlke/pythonlibs/

再这样安装：pip install pycryptosat‑0.2.0‑cp36‑cp36m‑win_amd64.whl



