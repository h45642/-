new_line = "这是新添加的一行内容\n"  
with open("python.txt", "a", encoding="UTF-8") as f:  
    f.write(new_line)
f =open("python.txt", "r", encoding="UTF-8")
content =f.readlines()
print(content)
f.close()
f=open("python.txt", "r", encoding="UTF-8")
content=f.readline()
print(f"第一行：{content}")
content =f.readline()
print(f"第二行:{content}")
f.close()
for line in open("python.txt","r",encoding="UTF-8"):
    print(line)
