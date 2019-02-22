# -*- coding: utf-8 -*-

import os 
# 1.利用os模块编写一个能实现dir -l 输出的程序
'''
import time
import win32file

def enum_dir(sPath):
    nFileCount = 0
    nFileSize = 0
    nFolderCount = 2

    curPath = os.path.abspath(sPath)
    print('\n',curPath,'的目录\n')
    szTime = time.strftime('%Y/%m/%d %H:%M',time.localtime(os.stat(curPath).st_mtime))
    print('%-20s%-7s%8s %s' % (szTime,'<DIR>','','.'))
    print('%-20s%-7s%8s %s' % (szTime,'<DIR>','','..'))

    with os.scandir(sPath) as it:
        for x in it:
            szTime = time.strftime('%Y/%m/%d %H:%M',time.localtime(x.stat().st_mtime))
            if not x.is_dir():
                fsize = x.stat().st_size
                print('%-20s%-7s%8s %s'%(szTime,'',fsize,x.name))
                nFileCount += 1
                nFileSize += fsize
            else:
                print('%-20s%-7s%8s %s'%(szTime,'<DIR>','',x.name))
                nFolderCount += 1
    
    sectorsPerCluster, bytesPerSector, numFreeClusters, totalNumClusters \
            = win32file.GetDiskFreeSpace(curPath)
    print('%15s 个文件 %14d 字节'%(nFileCount,nFileSize))
    print('%15s 个目录 %14d 可用字节'%(nFolderCount,numFreeClusters*sectorsPerCluster*bytesPerSector))


if __name__ == '__main__':
    enum_dir('.')
'''
# 2.编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
global COUNT    # 定义一个计数的全局变量，全部大写 
COUNT = 0
def search_dir(path,filename):
    for x in os.listdir(path):
        x = os.path.join(path,x)
        if os.path.isfile(x) and os.path.split(x)[1] == filename:
            print(x)
            COUNT += 1
        if os.path.isdir(x):
            search_dir(x,filename)
if COUNT == 0:
    print('File is not exist!')

if __name__ == '__main__':
    search_dir('.\\test','testy.py')


