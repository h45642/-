with open("word.txt", "r", encoding="utf-8") as f:
    # 读取文件的代码
    content = f.read()
    content = content.lower()
    # 统计"python"出现的次数
    count = content.count('python')
print(f"单词 'python' 出现 {count} 次.")

