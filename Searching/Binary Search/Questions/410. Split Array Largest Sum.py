# https://leetcode.com/problems/split-array-largest-sum/

from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        start, end = 0, 0
        for num in nums:
            if num > start:
                start = num
            end += num

        while start < end:
            mid = start + (end - start)//2

            # Calculate no of pieces
            sum = 0
            pieces = 1
            for num in nums:
                if sum + num > mid:
                    sum = num
                    pieces += 1
                else:
                    sum += num

            if pieces > m:
                start = mid + 1
            else:
                end = mid

        return start


s = Solution()
print(s.splitArray([1,2,3,4,5], 2))
