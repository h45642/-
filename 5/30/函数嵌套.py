def fun1(x,y):
    print("这是函数一")
    sum=x+y
    return  sum
def fun2():
    print("这是函数二")
    sum=fun1(2,3)
    print(sum)
fun2()

def max(x,y):
    return x if x>y else y
def maxs(a,b,c,d):
    res1 = max(a,b)
    res2 = max(res1,c)
    res3 = max(res2,d)
    return res3
print(maxs(5,2,420,299));

def f1():
    def f2():
        def f3():
            pass
    print("---->f1")
    f2()
# f2()#会报错，嵌套函数不能在外部使用