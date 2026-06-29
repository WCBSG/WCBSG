"""
8.文件操作
“天马来出月支窟，背为虎文龙翼骨。
嘶青云，振绿发，兰筋权奇走灭没。
腾昆仑，历西极，四足无一蹶。”
上述内容为李白的《天马歌》部分。请完成以下设计：
（1）定义文件file1.txt，将上述内容通过write的方式写入到文件中，要求按照本题的展示进行换行。
（2）定义一个新的文件file2.txt，新文件内容实现对file1.txt的拷贝。
"""

with open("file1.txt","w+") as file1, open("file2.txt","w+") as file2:
    file1.writelines(["天马来出月支窟，背为虎文龙翼骨。\n","嘶青云，振绿发，兰筋权奇走灭没。\n","腾昆仑，历西极，四足无一蹶。\n"])
    d = file1.readlines()
    file2.writelines(d)
