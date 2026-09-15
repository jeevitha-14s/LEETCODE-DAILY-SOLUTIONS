class Solution:
        def findContentChildren(self, g: list[int], s: list[int]) -> int:
            g.sort()
            s.sort()
            i = 0
            for c in s:
                if i < len(g) and c >= g[i]:
                    i += 1
            return i