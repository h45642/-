#猴子吃桃
def F(x):
    if x==1:
        return x
    else:
        return (F(x-1)+1)*2
print("请输入第几天的天数：")
n = int(input())
result = F(n)
print(f"第一天摘得果子数是：{result}")
