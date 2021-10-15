from typing import List

def BinarySearch(arr:List[int], target:int) -> int:

    start, end = 0, len(arr)-1

    while start <= end:
        mid = start + (end - start) // 2
        print(arr[start:end])
        if target > arr[mid]:
            start = mid + 1
        elif target < arr[mid]:
            end = mid - 1
        else:
            return mid
        
    return -1


if __name__ == '__main__':
    arr = [-12, -10, -6, -1, 0, 2, 5, 6, 25, 36, 52, 62, 75, 86]
    ret_val = BinarySearch(arr, target=25)

    if ret_val != -1:
        print(f'Element found at Index {ret_val}')
    else:
        print('Element does not found in Array')
