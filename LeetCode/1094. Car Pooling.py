'''
https://leetcode.com/problems/car-pooling/

Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
'''

from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        highway = [0] * 1001

        for n, i, j in trips:
            highway[i] += n
            highway[j] -= n

        for i in range(0, 1001):
            highway[i] += highway[i-1]
            if highway[i] > capacity:
                return False
        print(highway)

        return True


s = Solution()
trips = [[9,0,1],[3,3,7]]
capacity = 4
print(s.carPooling(trips, capacity))

