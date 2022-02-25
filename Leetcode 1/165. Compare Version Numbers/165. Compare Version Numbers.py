# https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = [int(x) for x in version1.split('.')]
        ver2 = [int(x) for x in version2.split('.')]
        print(f'ver1 = {ver1}, ver2 = {ver2}')
        for i in range(max(len(ver1), len(ver2))):
            v1 = ver1[i] if i < len(ver1) else 0
            v2 = ver2[i] if i < len(ver2) else 0
            print(f'{i}, {v1}, {v2}')
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
        return 0

s = Solution()
print(s.compareVersion(version1 = "0.1", version2 = "1.1"))