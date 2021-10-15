# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List

def searchRange(nums: List[int], target: int) -> List[int]:
    li = [-1, -1]
    
    start = search(nums, target, True)
    end = search(nums, target, False)
    
    li[0], li[1] = start, end
    
    
    return li

def search(arr: List[int], target: int, findstartindex: bool) -> int:
    
    ans = -1
    
    s, e = 0, len(arr)-1
    
    while s <= e:
        m = s + (e-s)//2
        
        if target > arr[m]:
            s = m + 1
        elif target < arr[m]:
            e = m - 1
        else:
            # Potential ans
            ans = m
            if findstartindex:
                e = m - 1
            else:
                s = m + 1
                
    return ans

if __name__ == '__main__':

    ret_val = searchRange(nums = [5,7,7,8,8,10], target = 8)
    print(ret_val)
    
    ret_val = searchRange(nums = [5,7,7,8,8,10], target = 6)
    print(ret_val)