class Solution:
        def isBalanced(self, root) -> bool:
            def depth(nd):
                if not nd:
                    return 0
                a = depth(nd.left)
                b = depth(nd.right)
                if a < 0 or b < 0 or abs(a - b) > 1:
                    return -1
                return 1 + max(a, b)
            return depth(root) >= 0