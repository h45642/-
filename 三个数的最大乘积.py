def threeride(nums):
    nums.sort()
    n = len(nums)
    max_product =float('-inf')

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                curr_product = nums[i] * nums[j] * nums[k]
                # 更新最大乘积
                if curr_product > max_product:
                    max_product = curr_product

    return max_product
nums = [0,1,1,1,9,9,9]
max_product = threeride(nums)
print("最大乘积为:" ,max_product)