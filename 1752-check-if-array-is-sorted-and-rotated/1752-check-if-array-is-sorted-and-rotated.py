class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len( nums)
        for x in range(n):
            sorted_ver = nums[x:] + nums[:x]

            if sorted_ver == sorted(nums):
                return True 
        return False
