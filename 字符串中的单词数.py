import re

def count_words(sentence):
    # 使用正则表达式找到所有由非空格字符组成的序列
    words = re.findall(r'\S+', sentence)
    # 返回找到的单词数量
    return len(words)

# 示例
input_sentence = "Hello, my name is John"
output = count_words(input_sentence)
print(output)  # 应该输出 5