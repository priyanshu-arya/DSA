li = []


def permutation(p ,up):
    if len(up) == 0:
        li.append(p)
        return

    for i in range(len(p)+1):
        f = p[:i]
        s = p[i:]
        permutation(f + up[0] + s, up[1:])


permutation('', 'rishikagupta')
print(li)
print(len(li))

