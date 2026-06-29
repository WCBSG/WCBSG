"""
8.班级值日表初始内容如下：
	周一：张三
	周二：李四
	周三：王五
请编写 Python 程序完成以下文件操作：
	（1）以写入模式创建文件duty_list.txt，将上述初始值日表内容写入文件（保留换行）；
	（2）以追加模式打开duty_list.txt，添加周四、周五的值日信息：
		周四：赵六
		周五：孙七
	（3）以读取模式打开文件，读取所有内容，统计文件的总行数并输出（示例：“值日表总行数：5”）；
	（4）所有文件操作需正确关闭文件（使用close()方法）。

"""

f = open("duty_list.txt","w")
f.writelines(["周一：张三\n","周二：李四\n","周三：王五\n"])
f.close()
    
f = open("duty_list.txt","a")
f.writelines(["周四：赵六\n","周五：孙七\n"])
f.close()

f = open("duty_list.txt","r")
d = f.readlines()
print(f"值日表总行数：{len(d)}")
f.close()
