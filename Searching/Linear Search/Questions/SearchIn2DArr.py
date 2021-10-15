from typing import List

def SearchIn2DArr(arr, target):
    if len(arr) == 0:
        return -1

    for row in range(len(arr)):
        for column in range(len(arr[row])):
            if arr[row][column] == target:
                return row, column

    return -1

if __name__ == '__main__':
    arr = [[10, 5, 26, 59, 32, 20],
    [36, 15, 313, 123, 62, 21],
    [2, 3, 5, 2, 6, 2, 3],
    [10, 65, 33],
    [9, 5, 6, 2, 63, 2, 2]]

    ret_val = SearchIn2DArr(arr, target = 200)

    print(ret_val)