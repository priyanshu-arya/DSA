from typing import List

class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        beauty = 0
        is_asc = False
        test_list = nums
        if(test_list == sorted(test_list)):
            is_asc = True
                
        for i in range(1, len(nums)-1):
            if nums[i-1] < nums[i] and nums[i] < nums[i+1] and is_asc:
                beauty += 2
                #print('1True')
            elif nums[i - 1] < nums[i] and nums[i] < nums[i + 1]:
                beauty += 1
                #print('2True')
            
        return beauty


s = Solution()
print(s.sumOfBeauties([1,2,3]))