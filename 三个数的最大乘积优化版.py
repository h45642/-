def threeride(nums):
    n = len(nums)
    if n < 3:
        return 0  # 或者抛出异常，因为无法找到三元组

    # 初始化最大乘积为前三个数的乘积（假设它们都是正数或零）
    max_product = float('-inf')
    if nums[0] >= 0:
        # 如果没有负数或者负数的乘积不会使结果更大，只需考虑最大的三个数
        max_product = max(max_product, nums[-1] * nums[-2] * nums[-3])
    else:
        # 初始化两个最小负数和最大正数的乘积
        max1, max2 = float('-inf'), float('-inf')
        for num in nums:
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2 and num != max1:
                max2 = num

                # 计算两个最小负数和最大正数的乘积，并与之前计算的最大乘积比较
        max_product = max(max_product, max1 * max2 * nums[-1])

        # 同时，也要考虑最大的三个数的乘积（如果它们都是正数或零）
        max_product = max(max_product, nums[-1] * nums[-2] * nums[-3])

    return max_product


nums = [0, 1, 1, 1, 9, 9, 9]
max_product = threeride(nums)
print("最大乘积为:", max_product)