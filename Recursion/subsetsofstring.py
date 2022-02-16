def subsets(string, ans, li =[]):
    if len(string) == 0:
        li.append(ans)
        return

    subsets(string[1:], ans)
    subsets(string[1:], ans+[string[0]])

    return li

print(subsets([1, 2, 3], []))
