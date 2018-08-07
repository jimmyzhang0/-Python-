#-- coding: utf-8 --

#设置函数add，显示出来add的两个具体参数
def add (a, b):
    print "ADDING %d + %d" % (a, b)
#不明白return作用
    return a + b
    
def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b
    
def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

#将函数add赋值并交给变量age
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

#A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

#复杂的一组运算
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes:", what, "Can you do it by hand？"
