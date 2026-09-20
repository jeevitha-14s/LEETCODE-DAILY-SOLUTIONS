class Solution:
        def largestRectangleArea(self, heights: list[int]) -> int:
            stack = []
            best = 0
            for i, h in enumerate(heights + [0]):
                start = i
                while stack and stack[-1][1] > h:
                    idx, ht = stack.pop()
                    best = max(best, ht * (i - idx))
                    start = idx
                stack.append((start, h))
            return best