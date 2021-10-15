# https://www.geeksforgeeks.org/find-position-element-sorted-array-infinite-numbers/

# Find position of an element in a sorted array of infinite numbers
'''
Suppose you have a sorted array of infinite numbers, how would you search an element in the array?
Source: Amazon Interview Experience. 
Since array is sorted, the first thing clicks into mind is binary search, but the problem here is that we don’t know size of array. 
If the array is infinite, that means we don’t have proper bounds to apply binary search. So in order to find position of key, first we find bounds and then apply binary search algorithm.
Let low be pointing to 1st element and high pointing to 2nd element of array, Now compare key with high index element, 
->if it is greater than high index element then copy high index in low index and double the high index. 
->if it is smaller, then apply binary search on high and low indices found. 
'''
from typing import List

def binarySearch(nums: List[int], target: int, start: int, end: int) -> int:

    while start <= end:
        mid = start + (end-start)//2

        if target > nums[mid]:
            start = mid + 1
        elif target < nums[mid]:
            end = mid - 1
        else:
            return mid

    return -1

def search(nums: List[int], target: int) -> int:
    start = 0
    end = 1

    # condition for the target in line to lie in the range
    while(target > nums[end]):
        new_start = end + 1
        #print('new_start', new_start)
        #double the box value
        #end = previousend + sizeofbox*2
        end = end + (end-start+1)*2
        #print('end', end)
        start = new_start
        #print('start', start)

    return  binarySearch(nums, target, start, end)
        


if __name__ == '__main__':
    li = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
    print(search(li, target=10))


'''Target Elemen can be taken carefully'''