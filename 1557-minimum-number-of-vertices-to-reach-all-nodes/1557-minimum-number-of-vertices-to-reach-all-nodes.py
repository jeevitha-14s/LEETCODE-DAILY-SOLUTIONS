class Solution:
        def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
            has_in = set(b for _, b in edges)
            return [i for i in range(n) if i not in has_in]