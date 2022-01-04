# https://www.geeksforgeeks.org/sum-triangle-from-array/
'''
Input : A = {1, 2, 3, 4, 5}
Output : [48]
         [20, 28]
         [8, 12, 16]
         [3, 5, 7, 9]
         [1, 2, 3, 4, 5]

Explanation :
Here,   [48]
        [20, 28] -->(20 + 28 = 48)
        [8, 12, 16] -->(8 + 12 = 20, 12 + 16 = 28)
        [3, 5, 7, 9] -->(3 + 5 = 8, 5 + 7 = 12, 7 + 9 = 16)
        [1, 2, 3, 4, 5] -->(1 + 2 = 3, 2 + 3 = 5, 3 + 4 = 7, 4 + 5 = 9)
'''

from typing import List


class Solution:
    def sumtrianglefromarray(self, arr: List[int]):
        if len(arr) == 0:
            return
        #print(arr)
        add = []
        for i in range(0, len(arr)-1):
            temp = arr[i] + arr[i+1]
            add.append(temp)

        self.sumtrianglefromarray(add)

        for num in arr:
            print(num, end=' ')
        print()


s = Solution()
nums = [5, 8, 1, 2, 4, 3, 14]
s.sumtrianglefromarray(arr= nums)