class Solution:
        def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
            target = len(graph) - 1
            res = []
            stack = [[0]]
            while stack:
                path = stack.pop()
                if path[-1] == target:
                    res.append(path)
                for v in graph[path[-1]]:
                    stack.append(path + [v])
            return res