"""
8.校园读书角需要整理推荐书单，书单内容如下：
	《Python编程：从入门到实践》
	《小王子》
	《平凡的世界》
	《解忧杂货店》
	《活着》
	请编写 Python 程序完成以下文件操作：
	（1）以写入模式打开（创建）文件book_list.txt，将上述书单内容逐行写入文件（每行一个书名，保留换行）；
	（2）以读取模式打开book_list.txt，逐行读取文件内容，打印每一行的书名（打印时去除换行符）；
	（3）所有文件操作需正确关闭文件（使用close()方法）。
"""

f = open("book_list.txt","w")
f.writelines(["《Python编程：从入门到实践》\n","《小王子》\n","《平凡的世界》\n","《解忧杂货店》\n","《活着》\n"])
f.close

f = open("book_list.txt","r")
d = f.readlines()
for i in range(len(d)):
    print(d[i].strip())
f.close
