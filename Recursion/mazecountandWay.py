class Solution:
    def countwayVH(self, row, column):
        if row == 1 or column == 1:
            return 1


        right = self.countwayVH(row, column-1)
        down = self.countwayVH(row-1, column)

        return right+down

    def countwayVHD(self, row, column):
        if row == 1 or column == 1:
            return 1


        right = self.countwayVHD(row, column-1)
        down = self.countwayVHD(row-1, column)
        if row > 1 and column > 1:
            diagonal = self.countwayVHD(row-1, column-1)
        return right+down+diagonal


    def way(self, processed, row, column, li):

        if row == 1 and column == 1:
            li.append(processed)
            return

        if row > 1:
            self.way(processed + 'V', row - 1, column, li)
        if column > 1:
            self.way(processed + 'H', row, column - 1, li)

        return li

    def diagonalway(self, processed, row, column, li):

        if row == 1 and column == 1:
            li.append(processed)
            return

        if row > 1:
            self.diagonalway(processed + 'V', row - 1, column, li)
        if column > 1:
            self.diagonalway(processed + 'H', row, column - 1, li)
        if row > 1 and column > 1:
            self.diagonalway(processed + 'D', row - 1, column - 1, li)
        return li

s = Solution()
print(s.countway(3,3))
print(s.way('', 3, 3, []))
