s ='helloworld'
s1 =s[0:5:2]
print(s1)
print(s[:5:1])
print(s[0:7:1])
print(s[0:6:])
print(s[::])

print("e在s中存在吗？",'e' in s)
print("v在s中存在吗？",'v' in s)
print("e在s中不存在吗？",'e' not in s)
print("v在s中存在吗？",'v' not in s)

print('len():',len(s))
print('max():',max(s))
print('min():',min(s))
print('s.index(o):',s.index('o'))
print('s.count(l):',s.count("l"))