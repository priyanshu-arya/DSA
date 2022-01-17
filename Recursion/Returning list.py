from typing import List


def findallindex(arr: List[int], target: int, index: int) -> List[int]:
    li = []

    if index == len(arr):
        return li

    if arr[index] == target:
        li.append(index)

    bc = findallindex(arr, target, index+1)
    li.extend(bc)
    return li


nums = [10, 15, 10, 20, 15, 65, 45, 65]
print(findallindex(nums, target=15, index=0))
