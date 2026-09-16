class Solution:
        def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
            INF = float('inf')
            cost = [INF] * n
            cost[src] = 0
            for _ in range(k + 1):
                nxt = cost[:]
                for u, v, w in flights:
                    if cost[u] + w < nxt[v]:
                        nxt[v] = cost[u] + w
                cost = nxt
            return -1 if cost[dst] == INF else cost[dst]