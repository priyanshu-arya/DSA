# https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        if columnTitle == '':
            return -1

        columnNumber = 0
        for ele in columnTitle:
            columnNumber *= 26
            columnNumber += ord(ele) - ord('A') + 1

        return columnNumber


if __name__ == '__main__':
    s = Solution()
    print(s.titleToNumber('ABC'))