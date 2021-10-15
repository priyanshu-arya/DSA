# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import BinaryIO, List

class Solution:
    def pivot(self, nums: List[int]) -> int:
        start, end = 0, len(nums)-1
        while start <= end:
            mid = start + (end-start)//2

            # 4 Cases over
            if mid < end and nums[mid] > nums[mid + 1]:
                return mid
            if mid > start and nums[mid] < nums[mid-1]:
                return mid-1
            
            # if elements are at middle, start and end are equal then skip them
            if nums[start] == nums[mid] and nums[start] == nums[end]:
                # skips the duplicates
                # check if start is the pivot element?
                if start < end and nums[start] > nums[start+1]:
                    return start
                start += 1

                if end > start and nums[end] < nums[end-1]:
                    return end - 1
                end -= 1

            elif nums[start] < nums[mid] or nums[start] == nums[mid] and nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid - 1

        return -1 

    
    def BinarySearch(self, nums: List[int], target: int, start: int, end: int) -> int:
        while start <= end:
            mid = start + (end-start)//2
            if target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                return mid
        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.pivot(nums)
        if pivot == -1:
            return self.BinarySearch(nums, target, 0, len(nums)-1)

        if nums[pivot] == target:
            return pivot

        if target >= nums[0]:    
            return self.BinarySearch(nums, target, 0, pivot-1)

        return self.BinarySearch(nums, target, pivot+1, len(nums)-1)
        

if __name__ == '__main__':
    narray = [4,5,6,7,7,0,1,2]
    target = 0
    s = Solution()
    find = s.search(narray, target)
    print(find)
