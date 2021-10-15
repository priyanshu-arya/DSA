# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.pivot_ele(nums)
        print(pivot)
        if pivot == -1:
            return self.BinarySearch(nums, target, 0, len(nums)-1)

        if nums[pivot] == target:
            return pivot

        if target >= nums[0]:   
            return self.BinarySearch(nums, target, 0, pivot-1)
        
        return self.BinarySearch(nums, target, pivot+1, len(nums)-1)
    
    def pivot_ele(self, nums: List[int]) -> int:
        start, end = 0, len(nums)-1
        
        while start < end:
            mid = start + (end-start) // 2
            # 4 cases over here
            if mid < end and nums[mid] > nums[mid + 1]:
                return mid
            
            if mid > start and nums[mid] < nums[mid - 1]:
                return mid -1

            if nums[mid] > nums[start]:
                end = mid
            else:
                start = mid + 1
                
        return -1
    
    def BinarySearch(self, nums: List[int], target: int, start: int, end: int):
        while start <= end:
            mid = start + (end - start)//2
            
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                return mid
            
        return -1
                
if __name__ == '__main__':
    narray = [4,5,6,7,0,1,2]
    target = 0
    s = Solution()
    find = s.search(narray, target)
    print(find)