'''
https://leetcode.com/problems/fibonacci-number/

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).



Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
'''


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        return self.fib(n-1) + self.fib(n-2)

if __name__ == '__main__':
    s = Solution()
    print(s.fib(3))