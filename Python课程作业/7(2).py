"""
7.统计班级学生的网课学习时长，编写 Python 函数实现以下列表相关的统计功能：
	定义名为calc_study_time的函数，接收一个参数：time_list（学生网课时长列表，元素为整数，单位：分钟，例如 [45, 60, 35, 80, 50, 75]）；
	函数内部完成以下操作：
		遍历列表，筛选出学习时长≥60 分钟的元素，生成新列表并返回；
		计算原列表中所有时长的平均值（保留 1 位小数），并返回；
	调用该函数，传入示例列表[45, 60, 35, 80, 50, 75]，并按格式输出结果：
		输出 “学习时长≥60 分钟的学生时长：[60, 80, 75]”；
		输出 “班级网课平均学习时长：57.5 分钟”。
"""

def calc_study_time(time_list=[]):
    newlist=[]
    sum=0
    for i in time_list:
        if i>=60:
            newlist.append(i)
        sum+=i
    vag=sum/len(time_list)
    return newlist,vag

newlist,vag = calc_study_time([45, 60, 35, 80, 50, 75])
print(f"学习时长≥60 分钟的学生时长：{newlist}")
print(f"班级网课平均学习时长：{vag}")
