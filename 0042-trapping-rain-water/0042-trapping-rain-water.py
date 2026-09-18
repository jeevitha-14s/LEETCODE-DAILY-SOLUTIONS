class Solution:
        def trap(self, height: list[int]) -> int:
            n = len(height)
            left = [0] * n
            right = [0] * n
            m = 0
            for i in range(n):
                m = max(m, height[i])
                left[i] = m
            m = 0
            for i in range(n - 1, -1, -1):
                m = max(m, height[i])
                right[i] = m
            return sum(min(left[i], right[i]) - height[i] for i in range(n))