#-- coding: utf-8 --

from sys import argv

script, filename = argv

#显示提示信息
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

#不理解输入一个文字，然后程序继续跑？
raw_input("?")

#先提示一下然后以只读方式打开文件
print "Opening the file..."
target = open(filename, 'w')

#清空文件内容
print "Truncating the file. Goodbye!"
target.truncate()

#提示一下，然后分别让你输入三次文字
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

#将三次输入的文字写入到打开的文本
print "I'm goling to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

#关闭文件写入操作
print "And finally, we close it."
target.close()
