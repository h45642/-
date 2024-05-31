# 例如：min_max（2,5,7,8,4）返回：{"max":"8," min"":2}
def func(*args):
    the_max=args[0]
    the_min=args[0]
    for i in args:
        if i>the_max:
            the_max=i
        elif i<the_min:
            the_min=i
    return{'max':the_max,'min':the_min}
res=func(1,20,3,40,5)
print(res)