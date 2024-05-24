from typing import List
def singleNumber(nums: List[int]) -> int:
    if len(nums) == 1:
        return  nums[0]
    nums.sort()
    for i in range(len(nums)):
        if i == len(nums) - 1:
            if nums[i] == nums[i-1]:
                continue
            else:
                return  nums[i]
        elif nums[i] == nums[i+1] or nums[i] == nums[i-1]:
            continue
        else:
            return  nums[i]
nums=[3,5,5,3,1,2,1]
print(singleNumber(nums))