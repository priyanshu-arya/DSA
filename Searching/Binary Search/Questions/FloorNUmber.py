
from typing import List

#greatest number <= target Element
def FloorNumber(arr: List[int], target: int) -> int:
    if target > arr[len(arr)-1]:
        return -1

    s, e = 0, len(arr)-1

    while s <= e:
        med = s + (e-s)//2

        if target > arr[med]:
            s = med + 1
        elif target < arr[med]:
            e = med - 1
        else:
            return med

    return e

if __name__ == '__main__':
    arr = [-12, -10, -6, -1, 0, 2, 5, 6, 25, 36, 52, 62, 75, 86]
    #arr_rev = arr[::-1]
    ret_val = FloorNumber(arr, target=36)

    if ret_val != -1:
        print(f'Floor Element found at Index {ret_val} and value is {arr[ret_val]}')
    else:
        print('Element does not found in Array')
