"""
4.已知预定义列表：fruit_list = ["苹果", "香蕉", "橙子", "葡萄"]，编写 Python 程序实现以下功能：
	向列表的第 2 个位置（索引为 1）插入元素 “草莓”；
	移除列表中的 “葡萄” 元素；
	向列表末尾追加元素 “芒果”；
	依次输出每一步操作后的完整列表（插入后、移除后、追加后）。
"""

fruit_list = ["苹果", "香蕉", "橙子", "葡萄"]
fruit_list.insert(1,"草莓")
print(fruit_list)
fruit_list.pop()
print(fruit_list)
fruit_list.append("芒果")
print(fruit_list)
