#--coding: utf-8 --


#让程序有参数功能
from sys import argv

#设定一个参数叫user_name
script, user_name = argv

#设定一个变量内容是一个提示符
prompt = '> '

#打印一句话并包含两个字符串一个是参数值，一个是程序名
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name

#让用户输入一个值并赋予变量likes
likes = raw_input(prompt)

print "Where do you live %s?" % user_name

#让用户输入一个值并赋予lives
lives = raw_input(prompt)

print "What kind of computer do you have?"

#让用户输入一个值并赋予computer
computer = raw_input(prompt)

#打印以下内容，并且把字符串都代入
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
