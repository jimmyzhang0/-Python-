# --coding: utf-8 --

#\t功能是制表符
tabby_cat = "\tI'm tabbed in."

#\n功能是换行
persian_cat = "I'm split\non a line."

#两次\\就会打印一个\出来，是转义功能
backslash_cat = "I'm \\ a \\ cat."

#三次"""用以显示带复杂字符串的字符串
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

