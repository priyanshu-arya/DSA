class Solution:
    def dice(self, p, target):
        if target == 0:
            li = []
            li.append(p)
            return li
        li = []
        for i in range(1,target+1):
            li.extend(self.dice(p + str(i), target-i))
        return li

    def diceface(self, p, target, face):
        if target == 0:
            li = []
            li.append(p)
            return li
        li = []
        for i in range(1,(face+1 and target+1)):
            li.extend(self.diceface(p + str(i), target-i, face))
        return li

s = Solution()
print(s.dice('', 4))
print(s.diceface('', 4, 6))