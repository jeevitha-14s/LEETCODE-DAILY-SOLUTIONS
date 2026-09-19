class Solution:
        def lowestCommonAncestor(self, root, p, q):
            parent = {root: None}
            stack = [root]
            while p not in parent or q not in parent:
                nd = stack.pop()
                for ch in (nd.left, nd.right):
                    if ch:
                        parent[ch] = nd
                        stack.append(ch)
            anc = set()
            while p:
                anc.add(p)
                p = parent[p]
            while q not in anc:
                q = parent[q]
            return q