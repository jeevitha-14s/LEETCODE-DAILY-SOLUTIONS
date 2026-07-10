class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        for r in range(n):

            rotated = nums[r:] + nums[:r]

            if rotated == sorted(rotated):
                return True

        return False
        