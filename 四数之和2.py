from typing import List
def fourSum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    result = []
    # 遍历数组，枚举前两个数
    for first in range(n - 3):
        # 跳过重复元素
        if first > 0 and nums[first] == nums[first - 1]:
            continue
            # 枚举第三个数
        for second in range(first + 1, n - 2):
            # 跳过重复元素
            if second > first + 1 and nums[second] == nums[second - 1]:
                continue
                # 初始化左右指针
            third = second + 1
            fourth = n - 1
            # 双指针查找第四个数
            while third < fourth:
                total = nums[first] + nums[second] + nums[third] + nums[fourth]
                if total == target:
                    # 找到一组解，添加到结果中
                    result.append([nums[first], nums[second], nums[third], nums[fourth]])
                    # 跳过重复元素
                    while third < fourth and nums[third] == nums[third + 1]:
                        third += 1
                    while third < fourth and nums[fourth] == nums[fourth - 1]:
                        fourth -= 1
                        # 重新检查 total，因为可能跳过重复元素后 total 仍然等于 target
                    total = nums[first] + nums[second] + nums[third] + nums[fourth]
                    if total == target:
                        # 注意：这里不应该有 continue 语句
                        pass  # 或者你可以完全移除这一行
                    # 移动指针
                    third += 1
                    fourth -= 1
                elif total < target:
                    third += 1
                else:
                    fourth -= 1
    return result
# 示例
nums = [1, 0, -1, 0, -2, 2]
target = 0
print(fourSum(nums, target))