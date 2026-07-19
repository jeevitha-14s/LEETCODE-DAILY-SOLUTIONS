class Solution:
    def maxAreaOfIsland(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        directions = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]

        def dfs(r, c):

            if (
                r < 0 or
                c < 0 or
                r >= rows or
                c >= cols or
                grid[r][c] == 0
            ):
                return 0

            grid[r][c] = 0

            area = 1

            for dr, dc in directions:
                area += dfs(r + dr, c + dc)

            return area

        answer = 0

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1:
                    answer = max(answer, dfs(r, c))

        return answer