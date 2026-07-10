class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        for r in range(n):

            rotated = nums[r:] + nums[:r]

            isSorted = True

            for i in range(n - 1):
                if rotated[i] > rotated[i + 1]:
                    isSorted = False
                    break

            if isSorted:
                return True

        return False