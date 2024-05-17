path = 'attack.csv'
ips = [line.strip() for line in open(path, 'r') if line.strip()]
data = set(ips)

data_dict ={}
for i in ips:
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