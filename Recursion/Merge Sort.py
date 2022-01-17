from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums, 0, len(nums))

    def mergeSort(self, nums: List[int]) -> List[int]:
        if len(nums) > 1:

            fhalf = self.mergeSort(nums[0:len(nums)//2])
            shalf = self.mergeSort(nums[(len(nums)//2):])
            return self.merge(fhalf, shalf)

    def merge(self, arr1, arr2):
        li = []
        i, j = 0, 0
        while (i < len(arr1)) and (j < len(arr2)):
            if arr1[i] < arr2[j]:
                li.append(arr1[i])
                i += 1
            else:
                li.append(arr2[j])
                j += 1

        while i < len(arr1):
            li.append(arr1[i])

        while j < len(arr2):
            li.append(arr2[j])

        return li


s = Solution()
print(s.mergeSort([5,4,8,8,7,9,6,5,6]))