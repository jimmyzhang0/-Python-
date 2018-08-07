#--coding: utf-8 --

#调用文件操作，文件参数和exists
from sys import argv
from os.path import exists

#程序使用两个参数源文件和目标文件
script, from_file, to_file = argv

#显示从什么文件拷贝到什么文件
print "Copying from %s to %s" % (from_file, to_file)

#we could do these two on one Line too, how?
#把两个功能设置为变量待调用input变量为打开文件indata变量为读取打开的文件
input = open(from_file)
indata = input.read()

#显示文件大小
print "The input file is %d bytes long" % len(indata)

#显示输出文件是否存在，使用exists来做判断
print "Does the output file exist? %r" % exists(to_file)
#显示警示，按回车继续，按CTRL-C取消
print "Ready, hit RETURN to continue, CTRL-C to abort."
#获取一个回车输入
raw_input()

#以写入权限打开目标文件
output = open(to_file, 'w')
#将变量indata写入文件中
output.write(indata)

#显示最后的完成
print "Alright, all done."

#输出关闭
output.close()
#写入关闭
input.close()
