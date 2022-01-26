from typing import List


class Solution:
    def sortArray(self, nums: List[int]):
        return self.QuickSort(nums, 0, len(nums)-1)

    def QuickSort(self, nums: List[int], l: int, h: int):
        if l < h:
            j = self.partition(nums, l, h)
            self.QuickSort(nums, l, j)
            self.QuickSort(nums, j+1, h)

    def partition(self, nums: List[int], l: int, h: int) -> int:
        pivot = nums[l]
        i, j = l, h

        while i < j:
            #i += 1
            while nums[i] <= pivot:
                i += 1

            #j -= 1
            while nums[j] <= pivot:
                j -= 1

            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

        nums[l], nums[j] = nums[j], nums[l]

        return j


s = Solution()
nums = [5,4,8,8,7,9,6,5,6]
s.sortArray(nums)
print(nums)