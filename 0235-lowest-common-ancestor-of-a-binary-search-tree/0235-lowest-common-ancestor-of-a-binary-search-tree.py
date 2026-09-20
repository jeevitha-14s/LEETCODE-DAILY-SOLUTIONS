class Solution:
        def lowestCommonAncestor(self, root, p, q):
            nd = root
            while nd:
                if p.val < nd.val and q.val < nd.val:
                    nd = nd.left
                    continue
                if p.val > nd.val and q.val > nd.val:
                    nd = nd.right
                    continue
                return nd
            return None