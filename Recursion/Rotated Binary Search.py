from typing import List


class Solution:

    def rotatedBS(self, nums: List[int], target: int, s: int, e: int):
        if s > e:
            return -1

        m = s + (e-s)//2
        if nums[m] == target:
            return m
        if nums[s] <= nums[m]:
            if target >= nums[s] and target <= nums[m]:
                return self.rotatedBS(nums, target, s, m-1)
            else:
                return self.rotatedBS(nums, target, m+1, e)

        if target >= nums[m] and target <= nums[e]:
            return self.rotatedBS(nums, target, m+1, e)

        return self.rotatedBS(nums, target, s, m-1)

s = Solution()
nums = [1,0,1,1,1]
print(s.rotatedBS(nums, target=0 , s=0, e=len(nums)-1))

