'''
Length of the longest substring without repeating characters
https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/
https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''

def is_distinct(s: str) -> bool:
    alphabet = [0] * 26

    for i in range(len(s)):
        if alphabet[ord(s[i]) - ord('a')] == True:
            return False
        else:
            alphabet[ord(s[i]) - ord('a')] = True
    
    return True


def unique_substring(s: str) -> int:
    max_s = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if is_distinct(s[i: j]):
                max_s = max(max_s, j-i)
    return max_s



def unique_sub2(s: str) -> int:
    seen = {}
    start = 0
    max_s = 0
    for i in range(len(s)):
        if s[i] in seen:
            start = max(start, seen[s[i]] + 1)
        
        seen[s[i]] = i
        max_s = max(max_s, i-start+1)
    return max_s

if __name__ == '__main__':
    s = 'pwwkew'
    print(unique_sub2(s))

