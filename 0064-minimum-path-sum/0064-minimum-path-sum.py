class Solution:
        def minPathSum(self, grid: list[list[int]]) -> int:
            INF = float('inf')
            n = len(grid[0])
            dp = [0] + [INF] * (n - 1)
            for row in grid:
                for j in range(n):
                    dp[j] = row[j] + min(dp[j], dp[j - 1] if j else INF)
            return dp[-1]