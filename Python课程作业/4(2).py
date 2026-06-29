"""
4.已知预定义列表：num_list = [8, 2, 9, 5, 1, 7]
编写 Python 程序实现以下功能：
	将该列表反转，并输出反转后的完整列表；
	移除列表中索引为 3 的元素，输出移除后的列表；
	统计列表中数字 “9” 出现的次数，并输出。
"""

def c9(num):
    c9=0
    for i in num:
        if i == 9:
            c9+=1
    return c9

num_list = [8, 2, 9, 5, 1, 7]
num_list=num_list[::-1]
print(num_list)
num_list.pop(3)
print(num_list)
print(c9(num_list))
