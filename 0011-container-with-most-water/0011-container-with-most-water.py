class Solution:
        def maxArea(self, height: list[int]) -> int:
            l, r, best = 0, len(height) - 1, 0
            while l < r:
                best = max(best, (r - l) * min(height[l], height[r]))
                l, r = (l + 1, r) if height[l] < height[r] else (l, r - 1)
            return best