'''
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
'''

class Solution:
    def numberOfSteps(self, num: int) -> int:
        return self.numberOfStepsCount(num)

    def numberOfStepsCount(self, num: int) -> int:
        return self.helperStepsCount(num = num, count = 0)

    def helperStepsCount(self, num: int, count:int) -> int:
        if num == 0:
            return count

        if num % 2 == 0:
            return self.helperStepsCount(num//2, count+1)
        return self.helperStepsCount(num-1, count+1)

s = Solution()
print(s.numberOfSteps(14))

