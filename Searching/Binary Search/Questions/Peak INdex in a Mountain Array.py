#https://leetcode.com/problems/peak-index-in-a-mountain-array/
#https://leetcode.com/problems/find-peak-element/

from typing import List

def peakElement(arr:List[int]) -> int:
    start, end = 0, len(arr) - 1

    while start < end:
        mid = start + (end -start) // 2
        #print(mid)
        if arr[mid] > arr[mid+1]:
            end = mid
        else:
            start = mid + 1
        
    return start

if __name__ == '__main__':
    arr = [24,69,100,99,79,78,67,36,26,19]
    print(arr[peakElement(arr)])