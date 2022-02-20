# https://leetcode.com/problems/minimize-deviation-in-array/

'''You are given an array nums of n positive integers.

You can perform two types of operations on any element of the array any number of times:

If the element is even, divide it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
If the element is odd, multiply it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].
The deviation of the array is the maximum difference between any two elements in the array.

Return the minimum deviation the array can have after performing some number of operations.'''
from heapq import heapify, heappush, heappop
from typing import List

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = []
        for num in nums:
            tmp = num
            while tmp % 2 == 0:
                tmp //= 2
            heap.append((tmp, max(num, tmp * 2)))
        print(heap)
        Max = max(i for i, j in heap)
        print(Max)
        heapify(heap)
        print(heap)
        ans = float("inf")

        while len(heap) == len(nums):
            num, limit = heappop(heap)
            ans = min(ans, Max-num)
            if num < limit:
                heappush(heap, (num*2, limit))
                Max = max(Max, num*2)

        return ans




s = Solution()
nums = [4,1,5,20,3]
print(s.minimumDeviation(nums))
