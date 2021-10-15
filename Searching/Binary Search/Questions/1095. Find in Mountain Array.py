# https://leetcode.com/problems/find-in-mountain-array/

from typing import List

def findMountainArray(nums: List[int]) -> int:
    start, end = 0, len(nums) - 1

    while start < end:
        mid = start + (end - start)//2

        if nums[mid] > nums[mid + 1]:
            end = mid
        else:
            start = mid + 1

    return start

def OrderAgnosticSearch(nums: List[int], start: int, end: int, target: int) -> int:

    is_asc = nums[start] < nums[end]

    while start < end:
        mid = start + (end-start)//2

        if nums[mid] == target:
            return mid

        if is_asc:
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if nums[mid] > target:
                start = mid + 1
            else:
                end = mid + 1
    return -1    

def search(nums: List[int], target:int) -> int:
    peak = findMountainArray(nums)
    first_try = OrderAgnosticSearch(nums, 0, peak, target)

    if first_try != -1:
        return first_try
    return OrderAgnosticSearch(nums, peak+1, len(nums)-1, target)


if __name__ == '__main__':
    narray = [1,2,3,4,5,3,1]
    target = 3
    find = search(narray, target)
    print(find)

