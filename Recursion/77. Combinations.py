# https://leetcode.com/problems/combinations/

'''Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.'''

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.helper(n, k, [], res, 1)
        return res

    def helper(self, n, k, li, res, start):
        if k == 0:
            res.append(li)
            return
        for i in range(start, n+1):
            self.helper(n , k-1, li+[i], res, i+1)


s = Solution()
print(s.combine(4, 2))
