class Solution:
        def zigzagLevelOrder(self, root) -> list[list[int]]:
            res = []
            level = [root] if root else []
            flip = False
            while level:
                vals = [nd.val for nd in level]
                res.append(vals[::-1] if flip else vals)
                flip = not flip
                nxt = []
                for nd in level:
                    if nd.left:
                        nxt.append(nd.left)
                    if nd.right:
                        nxt.append(nd.right)
                level = nxt
            return res