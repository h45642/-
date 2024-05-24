def test_func(compute):
    result = compute(1,2)
    print(result)
def compute(x,y):
    return  x+y
test_func(compute)

# lambda 关键字传入一个一次性使用的匿名函数
def test_func(compute):
    result = compute(1,2)
    print(result)
test_func(lambda  x,y:x+y)

from functools import reduce

total = reduce(lambda x, y: x + y, range(101))
print(total)


def test_func(compute):
    result = compute()
    print(result)
# 使用lambda表达式定义一个计算0到100和的函数（这里其实不推荐使用lambda）
test_func(lambda: sum(range(101)))