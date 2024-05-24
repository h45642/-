lst=[4,56,3,78,40,56,89]
print('原列表：',lst)

#排序
lst.sort()
print('升序：',lst)

#降序
lst.sort(reverse=True)
print('降序：',lst)

lst2=['banana','aple','Cat','Orange']
print('原列表:',lst2)
#升序排序，先排大写，再排小写
lst2.sort()
print('升序:',lst2)
#降序，先排小写，后排大写
lst2.sort(reverse=True)
print('降序',lst2)
#忽略大小写比较
lst2.sort(key=str.lower)
print(lst2)