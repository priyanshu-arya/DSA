# https://www.geeksforgeeks.org/find-rotation-count-rotated-sorted-array/

'''
Consider an array of distinct numbers sorted in increasing order. The array has been rotated (clockwise) k number of times. Given such an array, find the value of k.
Examples: 
 

Input : arr[] = {15, 18, 2, 3, 6, 12}
Output: 2
Explanation : Initial array must be {2, 3,
6, 12, 15, 18}. We get the given array after 
rotating the initial array twice.

Input : arr[] = {7, 9, 11, 12, 5}
Output: 4

Input: arr[] = {7, 9, 11, 12, 15};
Output: 0
'''
from typing import List

# find pivot element in the array the position of pivot elemen is the solution

def rotationCount(nums: List[int]) -> int:
    start, end = 0, len(nums)-1

    while start <= end:
        mid = start + (end-start) // 2

        if mid < end and nums[mid] > nums[mid+1]:
            return mid + 1
        if mid > start and nums[mid] < nums[mid-1]:
            return mid

        if nums[mid] > nums[start]:
            start = mid + 1
        else:
            end = mid - 1

    return -1


if __name__ == '__main__':
    print(rotationCount([7, 9, 11, 12, 5]))