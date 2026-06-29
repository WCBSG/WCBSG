"""
5.已知预定义字典：score_dict = {"Python":85, "高数":78, "英语":92}编写 Python 程序实现以下功能：
	获取并输出 "Python" 对应的分数；
	向字典中增加键值对 "计算机基础":88，输出增加后的字典；
	删除字典中分数最低的键值对（本题最低为 "高数":78），输出删除后的字典；
	输出字典的键值对总数（长度）。
"""
def del_low(zd):
    lowkey=""
    lowvalue=999
    for i in zd:
        if zd[i]<=lowvalue:
            lowkey=i
            lowvalue=zd[i]
    del zd[lowkey]
    return zd

score_dict = {"Python":85, "高数":78, "英语":92}

print(score_dict["Python"])
score_dict["计算机基础"]=88
print(score_dict)
print(del_low(score_dict))
print(len(score_dict))
