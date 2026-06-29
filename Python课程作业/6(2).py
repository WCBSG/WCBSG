"""
6.在日常生活中，我们经常需要计算商品的折后价格。
请编写一个 Python 函数，实现以下功能：
	定义一个名为calc_discount_price的函数，该函数接收一个参数：original_price（商品原价，整数 / 浮点数）；
	函数内部根据原价自动判断折扣：
	若原价 ≥ 200 元，按 8 折计算（折后价 = 原价 × 0.8）；
	若原价 < 200 元，按 9 折计算（折后价 = 原价 × 0.9）；
	函数返回计算后的折后价格；
	调用该函数，分别传入原价 150 元、原价 250 元，按指定格式输出结果（示例：“原价 150 元，折后价格为：135.0 元”）。
"""

def calc_discount_price(original_price:int|float):
    return original_price*(0.8 if original_price>=200 else 0.9)

for i in [150,250]:
    print(f"原价 {i} 元，折后价格为：{calc_discount_price(i)} 元")
