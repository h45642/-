from typing import List
def fourthSum(nums:List[int]) -> List[List[int]]:
    n = len(nums)
    nums.sort()
    ans = list()
    #已经从小到大排完顺序了
    #枚举 a
    for first in range(n):
        #需要和上次不一样
        if first > 0 and nums[first] == nums[first - 1]:
            continue
        #c对应的指针初始指向数组的最右端
        forth = n - 1#数组下标
        target = -nums[first]
        #枚举b
        for second in range(first +1,n):
            #要和上一次枚举的数不相同
            if second > first + 1 and nums[second] == nums[second -1]:
                 continue
                #需要保证b的指针在c的指针的左侧
            for third in range(second +1,n):
                if third>second + 1 and nums[third] == nums[third -1]:
                    continue
                while third < forth and nums[second] + nums[third] +nums[forth] > target:
                 #将c向左移动一位
                 third -= 1
                #如果指针重合，随着b后续的增加
            #就不会有满足a+b+c=0 并且b<c的c了，可以退出循环
                if third == forth:
                    break
                if nums[second] + nums[third] +nums[forth] == target:
                    ans.append([nums[first],nums[second],nums[third],nums[forth]])
    return ans
#示例
num = [-1,-2,0,1,2,-1,-4]
print(fourthSum(num))

