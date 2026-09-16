class Solution:
        def solve(self, board: list[list[str]]) -> None:
            m, n = len(board), len(board[0])
            stack = [(i, j) for i in range(m) for j in range(n) if (i in (0, m - 1) or j in (0, n - 1)) and board[i][j] == 'O']
            while stack:
                r, c = stack.pop()
                if 0 <= r < m and 0 <= c < n and board[r][c] == 'O':
                    board[r][c] = 'S'
                    stack.extend([(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)])
            for i in range(m):
                for j in range(n):
                    board[i][j] = 'O' if board[i][j] == 'S' else 'X'