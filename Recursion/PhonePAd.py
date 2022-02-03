class Solution:

    def pad(self, p, up, li):

        if up == '':
            li.append(p)
            return

        digit = int(up[0])

        for i in range((digit-1)*3, digit*3):
            ch = chr(97+i)
            self.pad(p + ch, up[1:], li)

        return li

    def retpad(self, p, up):

        if up == '':
            li = []
            li.append(p)
            return li

        digit = int(up[0])
        li = []

        for i in range((digit-1)*3, digit*3):
            ch = chr(97+i)
            li.extend(self.retpad(p + ch, up[1:]))

        return li

    def padCount(self, p, up):

        if up == '':
            return 1

        digit = int(up[0])
        count = 0
        for i in range((digit-1)*3, digit*3):
            ch = chr(97+i)
            count += self.padCount(p + ch, up[1:])

        return count



s = Solution()
print(s.pad('', '12', []))
print(s.retpad('', '12'))
print(s.padCount('', '12'))