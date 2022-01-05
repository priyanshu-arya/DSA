'''
https://leetcode.com/problems/n-th-tribonacci-number/

The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.



Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537

'''


class Solution:
    dp = [0] * 38
    dp[1], dp[2] = 1, 1

    def tribonacci(self, n: int) -> int:
        if n < 3:
            return Solution.dp[n]

        if Solution.dp[n] != 0:
            return Solution.dp[n]

        Solution.dp[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        print(Solution.dp)
        return Solution.dp[n]


if __name__ == '__main__':
    s = Solution()
    print(s.tribonacci(37))