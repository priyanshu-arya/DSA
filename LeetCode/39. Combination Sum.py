# https://leetcode.com/problems/combination-sum/
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.helper(candidates, target, [], res)
        return res

    def helper(self, candidates, required, li, res):
        if required < 0:
            return
        if required == 0:
            res.append(li)
            return

        for i in range(len(candidates)):
            self.helper(candidates[i:], required-candidates[i], li+[candidates[i]], res)

if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2,3,2], 7))