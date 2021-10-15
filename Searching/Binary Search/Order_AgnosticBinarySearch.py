from typing import List

''''
    When You don't know in which Order your array/ List is Sorted then
    we appl Order_Agnostic Binary Search. 
    If your start > end element then array/ List is in decreasing Order
    else array/ List in accending Order

'''
def Order_AgnosticBinarySearch(arr:List[int], target:int) -> int:
    start, end = 0, len(arr) - 1

    is_asc = arr[start] < arr[end]

    while start <= end:
        mid = start + (end-start)//2

        if arr[mid] == target:
            return mid
        
        if is_asc:
            if target > arr[mid]:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if target < arr[mid]:
                start = mid + 1
            else:
                end = mid - 1

    return -1 

if __name__ == '__main__':
    arr = [-12, -10, -6, -1, 0, 2, 5, 6, 25, 36, 52, 62, 75, 86]
    arr_rev = arr[::-1]
    ret_val = Order_AgnosticBinarySearch(arr_rev, target=25)

    if ret_val != -1:
        print(f'Element found at Index {ret_val}')
    else:
        print('Element does not found in Array')
