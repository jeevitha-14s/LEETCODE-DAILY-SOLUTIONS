class Solution:
        def minReorder(self, n: int, connections: list[list[int]]) -> int:
            adj = [[] for _ in range(n)]
            for a, b in connections:
                adj[a].append((b, 1))
                adj[b].append((a, 0))
            seen = [False] * n
            seen[0] = True
            stack = [0]
            res = 0
            while stack:
                u = stack.pop()
                for v, c in adj[u]:
                    if not seen[v]:
                        seen[v] = True
                        res += c
                        stack.append(v)
            return res