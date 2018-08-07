#-- coding: utf-8 --

#试程序带有参数
from sys import argv

#程序有一个参数，并赋予变量filename
script, filename = argv

#变量txt等于用函数open打开启动程序时的参数
txt = open(filename)

#显示启动程序时候代入的参数（文件名）
print "Here's your file %r:" % filename

#显示变量txt内容（变量txt就是刚刚打开的启动程序时候代入的文件）
print txt.read()

print "Type the filename again:"

#让用户输入文字并赋予变量file_again
file_again = raw_input("> ")

#打开刚刚输入的文件名并赋予变量txt_again
txt_again = open(file_again)

#显示txt_again的内容
print txt_again.read()
