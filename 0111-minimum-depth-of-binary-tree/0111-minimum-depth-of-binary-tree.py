class Solution:
        def minDepth(self, root) -> int:
            level = [root] if root else []
            depth = 0
            while level:
                depth += 1
                nxt = []
                for nd in level:
                    if not nd.left and not nd.right:
                        return depth
                    if nd.left:
                        nxt.append(nd.left)
                    if nd.right:
                        nxt.append(nd.right)
                level = nxt
            return 0