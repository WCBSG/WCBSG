"""
7.班级需要统计学生的手机话费消费情况，编写 Python 函数实现以下字典相关的统计功能：
	（1）定义名为calc_phone_fee的函数，接收一个参数：fee_dict（话费字典，格式为 {姓名：月话费金额，姓名：月话费金额...}，金额为整数，例如 {"张三":58, "李四":45, "王五":72, "赵六":65, "孙七":38}）；
	（2）函数内部完成以下操作：
		找出话费金额最高的学生姓名，返回该姓名；
		计算所有学生的平均话费（保留 1 位小数），返回该数值；
	（3）调用该函数，传入示例话费字典{"张三":58, "李四":45, "王五":72, "赵六":65, "孙七":38}，并按格式输出结果：
	输出 “话费最高的学生：王五”；
	输出 “班级平均话费：55.6 元”。
"""

def calc_phone_fee(fee_dict={}):
    maxkey=""
    maxvalue=-1
    sum=0
    for i in fee_dict:
        if fee_dict[i]>maxvalue:
            maxkey=i
            maxvalue=fee_dict[i]
        sum+= fee_dict[i]
    vag=sum/len(fee_dict)
    return maxkey,vag

maxkey,vag = calc_phone_fee({"张三":58, "李四":45, "王五":72, "赵六":65, "孙七":38})
print(f"话费最高的学生：{maxkey}")
print(f"班级平均话费：{vag}")
