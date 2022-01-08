class Solution:
    def capitalizeTitle(self, title: str) -> str:
        li = title.split(' ')
        for i in range(len(li)):
            if len(li[i]) <= 2:
                li[i] = li[i].lower()
            else:
                li[i] = li[i].capitalize()

        title = ' '.join(li)
        return title

s = Solution()
s.capitalizeTitle('hello my name is')