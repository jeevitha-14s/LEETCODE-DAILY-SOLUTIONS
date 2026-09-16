class Solution:
        def findCenter(self, edges: list[list[int]]) -> int:
            a, b = edges[0]
            return a if a in edges[1] else b