class Solution:
    def searchInesrt(self,nums:List[int],target:int) -> int;
        left,right = 0,len(nums) - 1
        while left <= right:
            mid = (left + right)
            if nums[mid] < target:
                left = mid +1
            elif nums[mid] > target:
                right = mid -1
            else:
                return mid

        return left