class Solution:
        def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
            n = len(obstacleGrid[0])
            dp = [1] + [0] * (n - 1)
            for row in obstacleGrid:
                for j in range(n):
                    dp[j] = 0 if row[j] else dp[j] + (dp[j - 1] if j else 0)
            return dp[-1]