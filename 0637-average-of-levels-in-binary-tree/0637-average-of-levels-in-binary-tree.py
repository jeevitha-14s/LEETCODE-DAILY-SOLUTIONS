class Solution:
        def averageOfLevels(self, root) -> list[float]:
            res = []
            level = [root] if root else []
            while level:
                res.append(sum(nd.val for nd in level) / len(level))
                nxt = []
                for nd in level:
                    if nd.left:
                        nxt.append(nd.left)
                    if nd.right:
                        nxt.append(nd.right)
                level = nxt
            return res