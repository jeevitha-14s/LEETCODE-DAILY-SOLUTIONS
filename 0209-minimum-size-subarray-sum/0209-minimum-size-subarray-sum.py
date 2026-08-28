class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr_sum = 0
        minlen = float("inf")

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum >= target:
                minlen = min(minlen, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return 0 if minlen == float("inf") else minlen
        