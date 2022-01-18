from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)

    def mergeSort(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        mid = len(nums) // 2
        fhalf = self.mergeSort(nums[0:mid])
        shalf = self.mergeSort(nums[mid:len(nums)])
        return self.merge(fhalf, shalf)

    def merge(self, arr1: List[int], arr2: List[int]):
        li = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                li.append(arr1[i])
                i += 1
            else:
                li.append(arr2[j])
                j += 1

        while i < len(arr1):
            li.append(arr1[i])
            i += 1

        while j < len(arr2):
            li.append(arr2[j])
            j += 1

        return li


s = Solution()
print(s.sortArray([5,4,8,8,7,9,6,5,6]))