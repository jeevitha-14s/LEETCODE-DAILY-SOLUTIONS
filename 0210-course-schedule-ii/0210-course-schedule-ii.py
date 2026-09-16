class Solution:
        def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
            adj = [[] for _ in range(numCourses)]
            indeg = [0] * numCourses
            for a, b in prerequisites:
                adj[b].append(a)
                indeg[a] += 1
            q = [i for i in range(numCourses) if indeg[i] == 0]
            for u in q:
                for v in adj[u]:
                    indeg[v] -= 1
                    if indeg[v] == 0:
                        q.append(v)
            return q if len(q) == numCourses else []