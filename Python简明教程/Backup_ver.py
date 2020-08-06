import os
import time
import zipfile

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
# 添加一条来自用户的注释以创建zip文件名
comment = input('Enter a comment -->')

# 检查是否有评论输入
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
            comment.replace(' ', '_') + '.zip'

# target = today + os.sep + now + '.zip'

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

# ----------利用zipfile模块来实现功能---------
z = zipfile.ZipFile(target, 'r')

# 获取压缩包内文件的名字
for f in z.namelist():
    print(f)

# infolist 返回压缩包内文件的信息 返回列表
# for i in z.infolist():
#     print(i.file_size, i.filename, i.header_offset)

# print(z.read(z.namelist()[2]))  # 读取列表中的指定序号的文件内容并输出到屏幕
z.printdir()  # 将zip内的文件信息输出到控制台上
# print(z.getinfo(z.namelist()[3]))  # 获取zip文档内指定文件的信息。返回一个zipfile.ZipInfo对象，它包括文件的详细信息

z.extract(z.namelist()[7], r'.')  # 解压指定的文件到指定目录下
z.close()

# ZipFile.extractall([path[, members[, pwd]]]) 
# 功能：解压zip文档中的所有文件到当前目录。
# 参数：
# members 默认值为zip文档内的所有文件名称列表，也可以自己设置，选择要解压的文件名称
# z.extractall(r'E:Backup')

# ----------用密码解密zip文件操作----
# zf = zipfile.ZipFile(os.path.join(today + os.sep, '160517_003.zip'), 'r')
# # pwd接收的数据应该是byte类型，需要将str类型转换为byte类型
# zf.setpassword(b'0000')  # zf.setpassword(pwd=str.encode('0000')) 
# try:
#     zf.extractall(r'E:Backup' + os.sep + ''.join(time.strftime('%Y%m%d')))
# except Exception as ex:
#     print(ex)
# zf.close()

# ----------zipfile 读取文件的二进制数据
# zf_read = zipfile.ZipFile(os.path.join(os.getcwd(), '163314_333.zip'), 'r')
# print(zf_read.getinfo(zf_read.namelist()[1]))
# data = zf_read.read(zf_read.namelist()[1])
# # (lambda f, b: (f.write(b), f.close()))(open(r'E:Backup' + os.sep + ''.join('008.txt'), 'wb'), data) #使用一行代码完成操作？？
# # with open(r'E:Backup' + os.sep + ''.join('008.txt'), 'wb') as f:
# #     f.write(data)
# zf_read.close()

# ----------将指定文件加入到zip文档中----------
zf_add = zipfile.ZipFile(os.path.join(os.getcwd(), '163314_666.zip'), 'w', zipfile.ZIP_DEFLATED)
zf_add.write(r'D:/test.doc', 'w.doc')
zf_add.close()
