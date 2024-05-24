path = 'attack.csv' #这行代码定义了一个字符串变量path，它包含了文件名'attack.csv'。这个文件预计包含了IP地址列表。
ips = [line.strip() for line in open(path, 'r') if line.strip()]
# #这是一个列表推导式，用于从attack.csv文件中读取所有非空的行，并去除每行两端的空白字符（如空格、制表符或换行符）。
# open(path, 'r')：以只读模式打开path指定的文件。
# for line in open(path, 'r')：迭代文件的每一行。
# line.strip()：去除每行两端的空白字符。
# if line.strip()：如果去除空白字符后的行不是空字符串（即原行至少包含一个非空白字符），则将其包含在ips列表中。
data = set(ips)
# 这行代码将ips列表转换为一个集合data，集合去重
data_dict ={}#空字典，用来储存ip地址
for i in ips:
#循环遍历ips列表，统计每个IP地址出现的次数，并将结果存储在data_dict中。
    if i in data_dict:
        data_dict[i] += 1
    else:
        data_dict[i] = 1
print(data_dict)
sorted_items = sorted(data_dict.items(), key=lambda x: x[1])
# 降序排序
print(sorted_items)
with open('new.csv', 'w') as f:
    for ip, count in sorted_items:
        f.write(f"{ip}: {count}\n")
