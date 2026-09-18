class Solution:
        def isValidSudoku(self, board: list[list[str]]) -> bool:
            seen = set()
            for i in range(9):
                for j in range(9):
                    v = board[i][j]
                    if v == '.':
                        continue
                    keys = ((0, i, v), (1, j, v), (2, i // 3, j // 3, v))
                    for key in keys:
                        if key in seen:
                            return False
                        seen.add(key)
            return True