d={1001:'李梅',1002:'王华',1003:'张峰'}
print(d)

d[1004]='张丽丽'
print(d)

keys=d.keys()
print(keys)
print(list(keys))
print(tuple(keys))

values=d.values()
print(values)
print(list(values))
print(tuple(values))

lst=list(d.items())
print(lst)

d=dict(lst)
print(d)

print(d.pop(1001))
print(d)

print(d.pop(1008,'不存在'))
print(d.popitem())
print(d)

d.clear()
print(d)
print(bool(d))