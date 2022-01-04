class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return self.bitwiseComplementBW2(n)
        #return self.bitwiseComplementBW(n)
        #return self.bitwiseComplementBF(n)

    # O(log n)
    def bitwiseComplementBW2(self, n: int) -> int:

        return (1 << len(bin(n)) >> 2) - n - 1

    # O(log n)
    def bitwiseComplementBW(self, n: int) -> int:
        x = 1
        while x < n:
            x = x * 2 + 1

        return x ^ n

    # Time: O(n) Space: O(len(n in binary))
    def bitwiseComplementBF(self, n: int) -> int:
        l = list(bin(n)[2:])
        print(l)

        for i in range(len(l)):
            if l[i] == '0':
                l[i] = '1'
            elif l[i] == '1':
                l[i] = '0'

        print(l)

        s = '0b' + ''.join(str(x) for x in l)
        print(s)

        return int(s, 2)

s = Solution()
print(s.bitwiseComplement(5))
