from functools import reduce
total = reduce(lambda x, y: x + y, range(101))
print(total)


def test_func(compute):
    result = compute()
    print(result)
# 使用lambda表达式定义一个计算0到100和的函数（这里其实不推荐使用lambda）
test_func(lambda: sum(range(101)))