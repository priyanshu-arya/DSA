from typing import List


def linearsearch(nums: List[int], target: int, index: int) -> int:
    if index == len(nums)-1:
        return -1

    if nums[index] == target:
        return index

    return linearsearch(nums, target, index+1)


def linearsearch2(nums: List[int], target: int) -> bool:
    if len(nums) == 0:
        return False

    if nums[0] == target:
        return True

    return linearsearch2(nums[1:], target)


li = []
def linearsearch3(nums: List[int], target: int, index: int):
    if index == len(nums):
        return

    if nums[index] == target:
        li.append(index)

    linearsearch3(nums, target, index+1)


nums = [5,4,8,8,7,9,6,5,6]
linearsearch3(nums, target=6, index=0)
print(li)
