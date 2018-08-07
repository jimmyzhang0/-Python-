#-- coding: utf-8 --
#this one is like your scripts with argv
#定义一个print_two函数,函数可以有N个变量
def print_two(*args):
    arg1, arg2, = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
#ok, that *args is actually pointless, we can just do this
#另一种方式直接给出函数的参数
def print_two_again(arg1, arg2):
    print "agr1: %r, arg2: %r" % (arg1, arg2)

#给函数只定义一个变量    
#this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1
    
#不给函数变量
#this one takes on arguments
def print_none():
    print "I got nothin'."
    
#直接调用函数既可以把函数的功能完整释放
print_two("Zed", "Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
