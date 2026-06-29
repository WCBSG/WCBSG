"""
6.快递公司按包裹重量收取运费，编写 Python 函数实现运费计算，功能要求如下：
	定义名为calc_express_fee的函数，接收一个参数：weight（包裹重量，单位：千克，正数，整数 / 浮点数）；
	函数内部根据重量计算运费：
	重量 ≤ 1kg：运费 10 元；
	1kg < 重量 ≤ 5kg：基础运费 10 元 + 超出 1kg 部分每千克加收 2 元；
	重量 > 5kg：基础运费 18 元 + 超出 5kg 部分每千克加收 1.5 元；
	函数返回计算后的运费金额；
	调用该函数，分别传入重量 0.8、3、6，按格式输出结果（示例：“包裹重量 0.8kg，运费：10.0 元”）。
"""

import math
def calc_express_fee(weight:int|float):
    if weight<0:
        return "err"
    if weight<=1:
        m=10
    elif weight<=5:
        m=10
        m+=math.ceil(weight-1)*2
    else :
        m=18
        m+=math.ceil(weight-5)*1.5
    return m

for i in [0.8,3,6]:
    print(f"包裹重量 {i}kg，运费：{calc_express_fee(i)} 元")
