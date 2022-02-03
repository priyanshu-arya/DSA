# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return self.helper('', s)

    def helper(self, p, un):
        if len(un) == 1:
            return 1

        maxlength = 0
        temp = 0
        if un[0] in p:
            temp = self.helper('', un[1:])

        length = self.helper(p + un[0], un[1:])

        maxlength = max(maxlength, length, temp)
        return maxlength


s = Solution()
print(s.lengthOfLongestSubstring('abcabcbb'))
