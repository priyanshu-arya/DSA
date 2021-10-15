'''
Find maximum (or minimum) sum of a subarray of size k

https://www.geeksforgeeks.org/find-maximum-minimum-sum-subarray-size-k/

Input  : arr[] = {100, 200, 300, 400}
         k = 2
Output : 700

Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}
         k = 4 
Output : 39
We get maximum sum by adding subarray {4, 2, 10, 23}
of size 4.

Input  : arr[] = {2, 3}
         k = 3
Output : Invalid
There is no subarray of size 3 as size of whole
array is 2. 

'''
from typing import List

def maxSum(nums: List[int], k: int) -> int:
    sum = 0
    for i in range(k):
        sum = sum + nums[i]

    answer = sum
    for i in range(k, len(nums)):
        sum = sum + nums[i] - nums[i-k]
        answer = max(answer, sum)
    
    return answer

import ran_list as rl

if __name__ == '__main__':
    nums = rl.rlist()
    k = 20
    print(nums, len(nums))
    print(k)
    ans = maxSum(nums, k)
    print(ans)
