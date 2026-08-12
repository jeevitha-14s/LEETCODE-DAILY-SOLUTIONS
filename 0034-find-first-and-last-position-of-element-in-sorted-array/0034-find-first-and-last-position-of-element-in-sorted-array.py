class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        def lowerBound(nums, target):
            low, high = 0, n - 1
            ans = n

            while low <= high:
                mid = (low + high) // 2
                if nums[mid] >= target:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return ans

        def upperBound(nums, target):
            low, high = 0, n - 1
            ans = n

            while low <= high:
                mid = (low + high) // 2
                if nums[mid] > target:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return ans

        lb = lowerBound(nums, target)

        # target not present
        if lb == n or nums[lb] != target:
            return [-1, -1]

        ub = upperBound(nums, target)
        return [lb, ub - 1]
