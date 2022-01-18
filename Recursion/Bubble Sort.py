from typing import List


class Solution:
    def bubbleSort(self, nums: List[int], r: int, c: int):
        if r == 0:
            return

        if c < r:
            if nums[c] > nums[c+1]:
                nums[c], nums[c+1] = nums[c+1], nums[c]

            self.bubbleSort(nums, r, c+1)

        else:
            self.bubbleSort(nums, r-1, 0)

s = Solution()
nums = [4,3,2,1]
s.bubbleSort(nums, len(nums)-1, 0)
print(nums)


