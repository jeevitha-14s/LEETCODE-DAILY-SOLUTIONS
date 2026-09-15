class Solution:
        def canPartition(self, nums: list[int]) -> bool:
            total = sum(nums)
            if total % 2:
                return False
            bits = 1
            for x in nums:
                bits |= bits << x
            return (bits >> (total // 2)) & 1 == 1