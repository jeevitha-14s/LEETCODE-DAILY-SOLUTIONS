class Solution:
        def minimumTotal(self, triangle: list[list[int]]) -> int:
            dp = triangle[-1][:]
            for row in reversed(triangle[:-1]):
                dp = [x + min(dp[j], dp[j + 1]) for j, x in enumerate(row)]
            return dp[0]