
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/
from typing import List
class Solution:
    def nextGreatestLetter(self, arr: List[str], target: str) -> str:
        s, e = 0, len(arr)-1

        while s <= e:
            med = s + (e-s)//2

            if target >= arr[med]:
                s = med + 1
            else:
                e = med - 1
            

        return arr[s % len(arr)]