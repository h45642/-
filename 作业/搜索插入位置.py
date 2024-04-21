from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid  # 找到目标值，返回其索引
            elif nums[mid] < target:
                left = mid + 1  # 目标值在右侧子数组中
            else:
                right = mid - 1  # 目标值在左侧子数组中或不存在于数组中

        return left  # 返回应插入的位置


# 示例
solution = Solution()
nums = [1, 3, 5, 6]
target = 5
print(solution.searchInsert(nums, target))  # 输出: 2

target = 2
print(solution.searchInsert(nums, target))  # 输出: 1

target = 7
print(solution.searchInsert(nums, target))  # 输出: 4