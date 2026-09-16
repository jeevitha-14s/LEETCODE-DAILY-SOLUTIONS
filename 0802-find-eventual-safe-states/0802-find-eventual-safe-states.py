class Solution:
        def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
            n = len(graph)
            rev = [[] for _ in range(n)]
            outdeg = [len(g) for g in graph]
            for u in range(n):
                for v in graph[u]:
                    rev[v].append(u)
            q = [i for i in range(n) if outdeg[i] == 0]
            for v in q:
                for u in rev[v]:
                    outdeg[u] -= 1
                    if outdeg[u] == 0:
                        q.append(u)
            return sorted(q)