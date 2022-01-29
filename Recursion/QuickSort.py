from typing import List


class Solution:
    def sortArray(self, nums: List[int]):
        return self.QuickSort(nums, 0, len(nums)-1)

    def QuickSort(self, nums: List[int], l: int, h: int):
        if l >= h:
            return

        pivot = nums[l]
        i, j = l, h

        while i <= j:
            # i += 1
            while nums[i] < pivot:
                i += 1

            # j -= 1
            while nums[j] > pivot:
                j -= 1

            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        self.QuickSort(nums, l, j)
        self.QuickSort(nums, i, h)


s = Solution()
nums = [5,4,8,8,7,9,6,5,6]
s.sortArray(nums)
print(nums)