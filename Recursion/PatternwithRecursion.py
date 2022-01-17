'''

* * * * *
* * * *
* * *
* *
*

'''

def pattern1(row: int, column: int):
    if row == 0:
        return
    if column < row:
        print('X', end=' ')
        pattern1(row, column+1)
    else:
        print()
        pattern1(row-1, 0)


pattern1(5, 0)