class Solution:
        def kthSmallest(self, root, k: int) -> int:
            stack = []
            nd = root
            while stack or nd:
                while nd:
                    stack.append(nd)
                    nd = nd.left
                nd = stack.pop()
                k -= 1
                if k == 0:
                    return nd.val
                nd = nd.right
            return -1