lst=['hello','world','python','php']
for item in lst:
    print(item)

for i in range(0,len(lst)):
    print(i,'--->',lst[i])

for index,item in enumerate(lst):
    print(index,item)
for index,item in enumerate(lst,start=1):
    print(index,item)

for index,item in enumerate(lst,1):
    print(index,item)