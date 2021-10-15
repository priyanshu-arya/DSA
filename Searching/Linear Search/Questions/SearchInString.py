def SearchInString(arr:str, target:str) -> bool:
    if len(arr) == 0:
        return False

    for ele in arr:
        if ele == target:
            return True

    return False

def SearchInString2(arr:str, target:str) -> int:
    if len(arr) == 0:
        return -1

    for index in range(len(arr)):
        if arr[index] == target:
            return index

    return -1

if __name__ == '__main__':
    arr = input()
    target = input()
    print('String is', arr)
    print('Target is', target)

    ret_val = SearchInString(arr, target)

    if ret_val:
        print('Item Found')
    else:
        print('Item not Found')

    ret_val2 = SearchInString2(arr, target)

    if ret_val2 != -1:
        print('Item Found at index ', ret_val2)
    else:
        print('Item not Found')