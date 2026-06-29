"""
5.已知预定义字典：student_dict = {"202401":"张三","202402":"李四","202403":"王五"}
编写 Python 程序实现以下功能：
	检测字典中是否包含键 "202404"，输出检测结果（True/False）；
	将字典中键 "202402" 对应的 value 修改为 "李小四"，输出修改后的字典；
	清空字典中所有键值对，输出清空后的字典。
"""

student_dict = {"202401":"张三","202402":"李四","202403":"王五"}
print(('202404' in student_dict))
student_dict["202402"]="李小四"
print(student_dict)
student_dict={}
print(student_dict)
