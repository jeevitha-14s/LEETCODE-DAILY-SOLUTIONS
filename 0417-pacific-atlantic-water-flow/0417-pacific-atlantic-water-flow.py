class Solution:
        def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
            m, n = len(heights), len(heights[0])
            def flood(starts):
                seen = set(starts)
                stack = list(starts)
                while stack:
                    r, c = stack.pop()
                    for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                        if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen and heights[nr][nc] >= heights[r][c]:
                            seen.add((nr, nc))
                            stack.append((nr, nc))
                return seen
            pac = flood([(0, j) for j in range(n)] + [(i, 0) for i in range(m)])
            atl = flood([(m - 1, j) for j in range(n)] + [(i, n - 1) for i in range(m)])
            return [list(p) for p in pac & atl]