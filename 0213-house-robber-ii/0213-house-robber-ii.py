class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def robLinear(houses):
            n = len(houses)
            dp = [0] * (n + 2)

            for i in range(n - 1, -1, -1):
                dp[i] = max(houses[i] + dp[i + 2], dp[i + 1])

            return dp[0]

        return max(
            robLinear(nums[:-1]),   # Exclude last house
            robLinear(nums[1:])     # Exclude first house
        )