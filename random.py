def maximizeDumpling(nums):
    maximum = max(nums)
    res = dict.fromkeys(range(0, len(nums) + 1), 0)
    for i in range(len(nums)):
        res[nums[i]] += 1
    result = 0
    i = maximum
    while i > 0:
        if res[i] > 0:
            result += i
            res[i - 1] -= 1
            res[i] -= 1
        else:
            i -= 1
    return result

# Driver code
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(maximizeDumpling(nums))