from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums + [0]) * max(nums + [0]) * max(nums + [0])  # 处理小于3个元素的情况

        # 对数组进行排序
        nums.sort()

        # 最大的三个数的乘积
        max_three = nums[-1] * nums[-2] * nums[-3]
        # 最小的两个数（可能是负数）与最大数的乘积
        min_two_max_one = nums[0] * nums[1] * nums[-1]

        # 返回两个结果中的较大值
        return max(max_three, min_two_max_one)

    # 注意这里使用列表而不是集合


nums = [-2,1,  0, 1]

# 创建一个 Solution 对象并调用其 maximumProduct 方法
solution = Solution()
result = solution.maximumProduct(nums)

# 打印结果
print(result)