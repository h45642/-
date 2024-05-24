d={10:'cat',20:'dog',30:'pet',20:'zoo'}
print(d)

lst1=[10,20,30,40]
lst2=['cat','dog','pet','zoo','car']
zipobj=zip(lst1,lst2)
print(zipobj)
d=dict(zipobj)
print(d)
#两种创建字典的方式

# 使用参数创建
d=dict(cat=10,dog=20)
print(d)

t=(10,20,30)
print({t:10})

print('max',max(d))
print('min',min(d))
print('len:',len(d))
del d