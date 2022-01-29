li = []
def subsets(string, ans):
    if string == '':
        li.append(ans)
        return

    subsets(string[1:], ans)
    subsets(string[1:], ans + string[0])

subsets('rishika', '')
print(len(li))