from typing import List

def LinearSearch(arr: List[int], target: int, str: int, end: int) -> int:
    
    if len(arr) == 0:
        return -1

    for index in range(str, end+1):
        if arr[index] == target:
            return index

    return -1

    
if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    target = int(input())
    str, end = map(int, input().split())
    print('Array is\n', arr)
    print(f'Target is {target}')
    print(f'Range is [{str}, {end}]')
    ret_val = LinearSearch(arr, target, str, end)

    if ret_val == -1:
        print('Element no Found')
    else:
        print(f'Element found at index{ret_val}: and value at index is {arr[ret_val]}')