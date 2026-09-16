class Solution:
        def findCircleNum(self, isConnected: list[list[int]]) -> int:
            n = len(isConnected)
            seen = [False] * n
            count = 0
            for s in range(n):
                if seen[s]:
                    continue
                count += 1
                seen[s] = True
                stack = [s]
                while stack:
                    u = stack.pop()
                    for v in range(n):
                        if isConnected[u][v] and not seen[v]:
                            seen[v] = True
                            stack.append(v)
            return count