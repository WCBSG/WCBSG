"""
4.已知两个预定义列表：course_list1 = ["Python编程", "高等数学", "英语"]course_list2 = ["计算机基础", "职业规划"]编写 Python 程序实现以下功能：
	将 course_list2 连接到 course_list1 的末尾，生成一个新的完整课程列表；
	向新列表的最后位置追加元素 “创新创业”；
	反转这个新列表，并输出最终的完整列表；
	输出新列表的总长度。
"""

course_list1 = ["Python编程", "高等数学", "英语"];course_list2 = ["计算机基础", "职业规划"]
newlist= course_list1+course_list2
newlist.append("创新创业")
newlist=newlist[::-1]
print(newlist)
print(len(newlist))
