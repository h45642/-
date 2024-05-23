def process_ip_counts(input_path, output_path):
    # 读取CSV文件中的所有IP地址，并去除空行
    with open(input_path, 'r') as file:
        ips = [line.strip() for line in file if line.strip()]
        # 使用集合去重
    unique_ips = set(ips)
    # 初始化一个字典来存储IP地址及其出现次数
    data_dict = {}
    # 统计每个IP地址的出现次数
    for ip in unique_ips:
        data_dict[ip] = ips.count(ip)  # 直接使用列表的count方法计算IP地址的出现次数
    # 对字典按值进行排序（升序）
    sorted_items = sorted(data_dict.items(), key=lambda x: x[1])
    print(data_dict)
    # 如果需要降序排序，可以添加一个reverse参数
    # sorted_items = sorted(data_dict.items(), key=lambda x: x[1], reverse=True)
    # 将排序后的IP地址及其出现次数写入新的CSV文件
    with open(output_path, 'w') as file:
        for ip, count in sorted_items:
            file.write(f"{ip}: {count}\n")
        # 使用示例
    return 0
input_file = 'attack.csv'
output_file = 'new.csv'
process_ip_counts(input_file, output_file)
