from typing import List

def FindMin(arr:List[int]) -> int:
    if len(arr) == 0:
        return -1

    min = arr[0]
    for i in range(1, len(arr)):
        if min > arr[i]:
            min = arr[i]
    
    return min

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]

    ret_val = FindMin(arr)

    if ret_val != -1:
        print(f'Minimum in array is {ret_val}')
    else:
        print('Array is Empty')
