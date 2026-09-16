class Solution:
        def isBipartite(self, graph: list[list[int]]) -> bool:
            color = [-1] * len(graph)
            for s in range(len(graph)):
                if color[s] != -1:
                    continue
                color[s] = 0
                stack = [s]
                while stack:
                    u = stack.pop()
                    for v in graph[u]:
                        if color[v] == -1:
                            color[v] = 1 - color[u]
                            stack.append(v)
                        if color[v] == color[u]:
                            return False
            return True