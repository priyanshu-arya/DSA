from typing import List

class Solution:
    def sort(self, nums: List[int]) -> List[int]:
        i = 0
        count = 0
        while i < len(nums):
            correct = nums[i] - 1
            if nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
                count += 1
            else:
                i += 1
        print(count)
        return nums

def main():
    s = Solution()
    nums = [5, 4, 6, 3, 2, 1]
    print(s.sort([2,2,1,2]))

main()