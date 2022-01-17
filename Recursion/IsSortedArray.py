from typing import List

def isSortedArray(nums: List[int], index: int) -> bool:
    if index == len(nums)-1:
        return True

    return nums[index] < nums[index+1] and isSortedArray(nums, index+1)

print(isSortedArray([1,2,3,8,9,16], 0))