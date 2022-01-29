def removeapple(string, ans):
    if string == '':
        print(ans)
        return

    if string[:5] == 'apple':
        return removeapple(string[5:], ans)
    return removeapple(string[1:], ans + string[0])

removeapple('akoadmsmapplecdmi', '')

def removeappnotapple(string, ans):
    if string == '':
        print(ans)
        return

    if not(string[:5] == 'apple') and string[:3] == 'app':
        return removeappnotapple(string[3:], ans)
    return removeappnotapple(string[1:], ans + string[0])

removeappnotapple('akoadmsmapplecdmiapp', '')