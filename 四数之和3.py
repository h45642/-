from typing import List
def fourSum(nums: List[int], target: int) -> List[List[int]]:
    n = len(nums)
    nums.sort()
    ans = list()
    # 枚举 a
    for first in range(n - 3):  # 注意这里改为 n-3
        # 需要和上次不一样
        if first > 0 and nums[first] == nums[first - 1]:
            continue
            # target 为当前需要寻找的三数之和
        target_for_three = target - nums[first]
        # c 对应的指针初始指向数组的最右端
        forth = n - 1
        # 枚举 b
        for second in range(first + 1, n - 2):  # 注意这里改为 n-2
            # 要和上一次枚举的数不相同
            if second > first + 1 and nums[second] == nums[second - 1]:
                continue
                # 初始化 d 的指针位置
            third = second + 1
            # 枚举 c
            while third < forth:
                # 如果当前三数之和小于目标值，移动 c 的指针
                if nums[second] + nums[third] + nums[forth] < target_for_three:
                    third += 1
                    while third < forth and nums[third] == nums[third - 1]:
                        third += 1
                        # 如果当前三数之和大于目标值，移动 d 的指针
                elif nums[second] + nums[third] + nums[forth] > target_for_three:
                    forth -= 1
                    while third < forth and nums[forth] == nums[forth + 1]:
                        forth -= 1
                else:
                    # 找到满足条件的四元组
                    ans.append([nums[first], nums[second], nums[third], nums[forth]])
                    # 跳过重复元素
                    third += 1
                    while third < forth and nums[third] == nums[third - 1]:
                        third += 1
                    forth -= 1
                    while third < forth and nums[forth] == nums[forth + 1]:
                        forth -= 1
    return ans
# 示例
nums = [-1, -2, 0, 1, 2, -1, -4]
target = 0
print(fourSum(nums, target))