#-- coding: utf-8 --
#设定一个函数会有两个参数函数会显示出来两个参数
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

#给函数两个值    
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

#设置两个变量，把两个变量代入到函数中
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

#调用函数并且显示两个代入
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#直接给函数代入一个数学计算
print "We can even do math inside too:"

cheese_and_crackers(10 + 20, 5 + 6)

#给函数代入一个变量加数学运算
print "And we can combine the two, variables and math:"

cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
