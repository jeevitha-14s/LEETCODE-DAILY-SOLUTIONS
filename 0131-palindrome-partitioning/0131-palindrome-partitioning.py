class Solution:
        def partition(self, s: str) -> list[list[str]]:
            res = []
            def go(i, path):
                if i == len(s):
                    res.append(path[:])
                    return
                for j in range(i + 1, len(s) + 1):
                    piece = s[i:j]
                    if piece == piece[::-1]:
                        path.append(piece)
                        go(j, path)
                        path.pop()
            go(0, [])
            return res