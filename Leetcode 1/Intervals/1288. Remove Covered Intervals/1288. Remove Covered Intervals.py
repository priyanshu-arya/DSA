# https://leetcode.com/problems/remove-covered-intervals/
from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        print(f'Before sorting {intervals}')
        intervals.sort(key=lambda i: (i[0], -i[1]))
        print(f'After sorting {intervals}')
        res = [intervals[0]]

        for s, e in intervals[1:]:
            prevs, preve = res[-1]
            print(f'Previous Interval {res[-1]} and Current Interval {[s, e]}')
            if prevs <= s and preve >= e:
                continue
            print(f'Adding interval {[s, e]} in result')
            res.append([s, e])

        print(f'Final Result List is {res}')
        return len(res)


if __name__ == '__main__':
    s = Solution()
    intervals = [[3, 4], [4, 6], [2, 5], [2, 3]]
    intervals2 = [[3, 4], [4, 6], [2, 5], [2, 3], [1, 2], [3, 6], [5, 6]]
    print(s.removeCoveredIntervals(intervals2))