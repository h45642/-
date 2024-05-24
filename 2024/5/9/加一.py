# 获取用户输入的整数
input_number = input("请输入一个整数：")
# 将输入的字符串转换为整数
digits = int(input_number)
# 将整数加一
digits += 1
# 将加一后的整数转换为字符串
lst1 = str(digits)
# 将字符串转换为字符列表
lst2 = list(lst1)
# 打印结果列表
print(lst2)