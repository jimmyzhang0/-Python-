# --coding: utf-8 --

# 给变量 x 赋予一段文字
x = "There are %d types of people." % 10

# 给变量 binary 赋予 字符段 binary
binary = "binary"

# 给变量 do_not 赋予 字符段 don't
do_not = "don't"

# 给变量 y 赋予
y = "Those who know %s and those who %s." % (binary, do_not)

# 显示变量 x
print x

# 显示变量 y
print y

# 显示字符串套变量 x
print "I said: %r." % x

# 显示字符串套变量 y
print "I also said: '%s'." % y

# 赋予变量 hilarious 一个值 False
hilarious = False

# 赋予变量 joke_evaluation 一段字符串
joke_evaluation = "Isn't that joke so funny?! %r"

# 显示变量 joke_evaluation 套变量 hilarious
print joke_evaluation % hilarious

# 给变量 w 赋予一段字符串
w = "This is the left side of..."

# 给变量 e 赋予一段字符串
e = "a string with a right side."

# 依次显示变量w和e
print w + e
