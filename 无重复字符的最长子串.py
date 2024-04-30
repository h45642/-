def length_of_longest_substring(s): #定义一个函数
    start = 0 #双指针起始索引
    max_length = 0 #记录遍历过程中找到的无重复字符串
    char_set = set() #一个集合，存储当前子串中的字符

    for end in range(len(s)):  #遍历字符串s，end为结束索引
        while s[end] in char_set: #给循环加个条件 检查数组中是否在set出现过，即为重复
            char_set.remove(s[start]) #出现过，把初始索引从已有集合中删除，并使索引加一，向右移位
            start += 1
        char_set.add(s[end])#当最后的索引不在重复结束条件，使end索引加入集合
        max_length = max(max_length, end - start + 1) #max()比较两个数组，看看哪个更大就输出哪个，

    return max_length

print(length_of_longest_substring("abcabcbb"))  # 输出: 3
print(length_of_longest_substring("bbbbb"))     # 输出: 1
print(length_of_longest_substring("pwwkew"))    # 输出: 3