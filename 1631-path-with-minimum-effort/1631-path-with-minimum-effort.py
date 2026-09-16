import heapq
class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        m, n = len(heights), len(heights[0])
        best = [[float('inf')] * n for _ in range(m)]
        best[0][0] = 0
        heap = [(0, 0, 0)]
        while heap:
            e, r, c = heapq.heappop(heap)
            if r == m - 1 and c == n - 1:
                return e
            if e > best[r][c]:
                continue
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < m and 0 <= nc < n:
                    ne = max(e, abs(heights[nr][nc] - heights[r][c]))
                    if ne < best[nr][nc]:
                        best[nr][nc] = ne
                        heapq.heappush(heap, (ne, nr, nc))
        return 0