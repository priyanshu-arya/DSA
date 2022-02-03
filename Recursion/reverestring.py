def reverseString(s):
    l = len(s)
    if l < 2:
        return s
    return reverseString(s[l // 2:]) + reverseString(s[:l // 2])

print(reverseString(list('hello')))
