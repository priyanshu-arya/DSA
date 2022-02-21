#https://leetcode.com/problems/majority-element/

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return self.majorityElementMoore(nums)
        return self.majorityElementSorting(nums)
        return self.majorityElementBruteForce(nums)

    # counting frequency hash map BruteForce Approach
    # Time: O(n) Space: O(n)
    def majorityElementBruteForceHM(self, nums: List[int]) -> int:
        countdict = {}
        # counting frequency of each element
        for ele in nums:
            countdict[ele] = 1 + countdict.get(ele, 0)
        # Finding max element using freq
        maxfreq = float('-inf')
        for ele, freq in countdict.items():
            if freq > maxfreq:
                maxele, maxfreq = ele, freq

        return maxele

    # Sorting Nums
    # Time: O(nlogn) Space: O(1)
    def majorityElementSorting(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

    # Moore Voting Algoritm
    # Time: O(n) Space: O(1)
    def majorityElementMoore(self, nums: List[int]) -> int:
        freq, curr = 0, None

        for num in nums:
            if freq == 0:
                curr = num
            if curr == num:
                freq += 1
            else:
                freq -= 1

        return curr


if __name__ == '__main__':
    s = Solution()
    nums = [2, 2, 2, 1, 1, 1, 5, 4, 2]
    print(s.majorityElementSorting(nums))
    print(s.majorityElementMoore(nums))
    print(s.majorityElementBruteForceHM(nums))


