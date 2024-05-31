from datetime import datetime, date  # 直接从 datetime 模块导入 datetime 和 date

# 获取当前日期和时间
a = datetime.today()
print(a)
print(a.year)
print(a.month)
print(a.day)

# 创建两个日期对象
a = date(2017, 3, 1)
b = date(2017, 3, 15)

# 使用比较方法
print(a.__eq__(b))  # 等于
print(a.__ge__(b))  # 大于或等于
print(a.__gt__(b))  # 大于
print(a.__le__(b))  # 小于或等于
print(a.__lt__(b))  # 小于
print(a.__ne__(b))  # 不等于
print(a.__sub__(b))
print(a.__rsub__(b))

print(a.__format__('%Y-%m-%d'))
print(a.__format__('%Y/%m/%d'))
print(a.__format__('%Y/%m/%d'))
print(a.__format__('%D'))
print(a.__format__('%d'))

from  datetime import  time
a=time(12,20,30,899)
print(a)

from  datetime import *
d=date(2012,12,12)
print(d)
d1=d+timedelta(days=-1)
print(d1)
d2=d+timedelta(days=1)
print(d2)

from datetime import *
dt =datetime(2012,12,12,23,59,59)

dt1 = dt+timedelta(days=-1)
print(dt1)
dt2 = dt+timedelta(days=1)
print(dt2)
dt3 = dt+timedelta(hours=-1)
print(dt3)
dt4 = dt+timedelta(hours=1)
print(dt4)
dt5 = dt+timedelta(seconds=-1)
print(dt5)
dt6 = dt+timedelta(seconds=1)
print(dt6)



