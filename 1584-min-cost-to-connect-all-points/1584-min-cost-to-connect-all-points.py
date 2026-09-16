class Solution:
        def minCostConnectPoints(self, points: list[list[int]]) -> int:
            n = len(points)
            INF = float('inf')
            dist = [INF] * n
            used = [False] * n
            dist[0] = 0
            total = 0
            for _ in range(n):
                u = min((dist[i], i) for i in range(n) if not used[i])[1]
                used[u] = True
                total += dist[u]
                x, y = points[u]
                for v in range(n):
                    if not used[v]:
                        d = abs(points[v][0] - x) + abs(points[v][1] - y)
                        if d < dist[v]:
                            dist[v] = d
            return total