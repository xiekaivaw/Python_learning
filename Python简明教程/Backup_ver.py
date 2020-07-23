import os
import time

# 1. 需要备份的文件和目录将被指定在一个列表中
source = [r'D:\python\channel_list']
# source = ['"D:\\python\channel_list"'] # 在Windows下可以使用C:\\Document或者r'C:Document' 代表路径

# 2. 备份文件必须存储在一个主备份目录中
target_dir = 'E:\\Backup'
# 如果目标目录不存在，则进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # 创建目录

# 3.备份文件将打包压缩成zip文件
# 4.将当前日期作为主备份目录下的子目录名称
# os.sep 会根据操作系统给出相应的分隔符，在linxu下是'/',在Windows下会是'\\',在macos中会是':',使用os.sep会使得程序的可移植性变高
today = target_dir + os.sep + time.strftime('%Y%m%d')
# 当前时间作为zip文件的名称
now = time.strftime('%H%M%S')

# Zip文件的格式
target = today + os.sep + now + '.zip'

# 如果子目录不存在则创建一个
if not os.path.exists(today):
    os.mkdir(today)
    print('Successful created directory', today)

# 5. 使用zip命令将文件打包成zip格式的文件
zip_command = 'zip -r {0} {1}'.format(target, ''.join(source))

# 运行备份
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successsful backup to', target)
else:
    print('Backup FAILED')
