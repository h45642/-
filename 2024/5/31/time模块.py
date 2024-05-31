import calendar
import time

a =time.time()
for x in range(100000):
    pass
b=time.time() -a
print(b)

print(time.perf_counter())
print(time.perf_counter())
print(time.perf_counter())

print(time.gmtime())
print(time.localtime())
a=time.time()
time.localtime(a)

print(time.time())
print(time.ctime(time.time()))

a=time.strftime("%Y-%m-%d",time.gmtime())
print(a)

b=time.strftime("%Y-%m-%d %X")
print(b)

c=time.strftime("%X %X")
print(c)



import calendar

# 打印2021年11月的日历
print(calendar.month(2021, 11))

# 如果你想将日历存储在一个变量中以便后续使用，可以这样做
thismonth = calendar.month(2021, 11)
print(thismonth)  # 但注意，thismonth将是一个字符串，直接打印它可能不会在控制台上以很好的格式显示

# 如果你想要以更可读的格式打印日历，通常你会直接调用calendar.month()并传递文件对象（如sys.stdout）
# 但由于print函数默认将内容发送到sys.stdout，所以我们通常只是直接调用calendar.month()而不存储结果