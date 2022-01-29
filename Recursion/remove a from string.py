def removea(string, ans):
    if string == '':
        print(ans)
        return

    if string[0] == 'a':
        return removea(string[1:], ans)
    return removea(string[1:], ans+string[0])

removea('baccad', '')