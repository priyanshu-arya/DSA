'''
https://leetcode.com/problems/add-binary/
'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = list(a), list(b)
        carry = 0
        result = ''

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            result += str(carry%2)
            carry //= 2

        return result[::-1]

s = Solution()
print(s.addBinary('111', '111'))


