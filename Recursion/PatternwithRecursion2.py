'''

*
* *
* * *
* * * *
* * * * *

'''


def pattern1(row: int, column: int):
    if row == 0:
        return

    if column < row:
        pattern1(row, column+1)
        print('X', end=' ')
    else:
        pattern1(row-1, 0)
        print()

pattern1(5, 0)