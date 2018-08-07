#-- coding: utf-8 --

#设置程序带一个参数叫input_file
from sys import argv

script, input_file = argv

#设置一个函数功能是读取文件从开头到结尾并且显示出来
def print_all(f):
    print f.read()

#设置一个函数功能是移动游标位置    
def rewind(f):
    f.seek(0)

#设置了一个函数有两个参数并且显示出来两个参数    
def print_a_line(line_count, f):
    print line_count, f.readline()
    
#变量等于打开文件
current_file = open(input_file)

#显示一行字并且换行
print "First let's print the whole file:\n"

#调用函数print_all功能是显示原文件的所有内容
print_all(current_file)

#显示一行字
print "Now let's rewind, king of like a tape."

rewind(current_file)

#显示一行字
print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
