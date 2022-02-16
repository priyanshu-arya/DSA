class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        nums = [x for x in range(A + 1)]
        while len(nums) != 1:
            i = len(nums) - 1
            nums.remove(nums[i])
            nums.insert(0, nums.pop())
            print(nums)

        return nums[0]

s = Solution()
s.solve(11)
