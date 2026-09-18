class Solution:
        def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
            res = []
            top, bot, lft, rgt = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
            while top <= bot and lft <= rgt:
                for j in range(lft, rgt + 1):
                    res.append(matrix[top][j])
                top += 1
                for i in range(top, bot + 1):
                    res.append(matrix[i][rgt])
                rgt -= 1
                if top <= bot:
                    for j in range(rgt, lft - 1, -1):
                        res.append(matrix[bot][j])
                    bot -= 1
                if lft <= rgt:
                    for i in range(bot, top - 1, -1):
                        res.append(matrix[i][lft])
                    lft += 1
            return res