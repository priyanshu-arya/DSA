from typing import List


class Solution:
    def selectionSort(self, nums: List[int], r: int, c: int, max: int):
        if r == 0:
            return

        if c < r:
            if nums[c] > nums[max]:
                self.selectionSort(nums, r, c+1, c)
            else:
                self.selectionSort(nums, r, c+1, max)
        else:
            nums[max], nums[r-1] = nums[r-1], nums[max]
            self.selectionSort(nums, r-1, 0, 0)

s = Solution()
nums = [4,3,2,1]
s.selectionSort(nums, len(nums), 0, 0)
print(nums)


