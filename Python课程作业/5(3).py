"""
5.已知预定义字典：building_dict = {"001":"教学楼1","002":"教学楼2","003":"教学楼3"}，编写 Python 程序实现以下功能：
（1） 遍历字典，分别输出所有的 key（键）和 value（值）（格式示例："所有键：001 002 003"、"所有值：教学楼 1 教学楼 2 教学楼 3"）；
（2） 向字典中增加键值对 "004":"教学楼 4"，并输出增加后的完整字典；
（3） 删除字典中键为 "002" 的键值对，输出删除后的完整字典。
"""

building_dict = {"001":"教学楼1","002":"教学楼2","003":"教学楼3"}
print("所有键：",end="")
_=[print(i,end=" ") for i in building_dict.keys()]
print("、所有值：",end="")
_=[print(i,end=" ") for i in building_dict.values()]
print("")
building_dict["004"]="教学楼 4"
print(building_dict)
del building_dict["002"]
print(building_dict)
