# n的阶乘
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)#递归函数
num=5
result=factorial(num)
print(f"The factorial of {num} is:{result}")

