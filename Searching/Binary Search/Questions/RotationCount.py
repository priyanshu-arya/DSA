from typing import List

class Solution:
    def rotationCount(self, nums: List[int]) -> int:
        return self.findpivot(nums) + 1

    def findpivot(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1

        while low < high:
            mid = low + (high-low) // 2

            if mid < high and nums[mid] > nums[mid + 1]:
                return mid
            
            if mid > low and nums[mid] < nums[mid - 1]:
                return mid - 1

            if nums[mid] <= nums[low]:
                high = mid - 1
            else:
                low = mid + 1

        return -1


if __name__ == '__main__':
    narray = [3,4,5,6]
    target = 2
    s = Solution()
    rotation = s.rotationCount(narray)
    print(rotation)
