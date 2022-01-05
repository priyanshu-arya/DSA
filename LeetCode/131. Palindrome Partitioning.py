'''
https://leetcode.com/problems/palindrome-partitioning/

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]

'''

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        return self.partitionBT(s)

    def partitionBT(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(i: int):
            if i >= len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res

    def isPali(self, s: str, l: int, r: int) -> bool:

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.partition('aabnncsncsllll'))

