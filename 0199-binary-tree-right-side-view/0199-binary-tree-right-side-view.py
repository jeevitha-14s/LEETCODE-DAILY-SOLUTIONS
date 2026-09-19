class Solution:
        def rightSideView(self, root) -> list[int]:
            res = []
            level = [root] if root else []
            while level:
                res.append(level[-1].val)
                nxt = []
                for nd in level:
                    if nd.left:
                        nxt.append(nd.left)
                    if nd.right:
                        nxt.append(nd.right)
                level = nxt
            return res