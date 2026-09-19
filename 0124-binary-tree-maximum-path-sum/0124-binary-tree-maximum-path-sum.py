class Solution:
        def maxPathSum(self, root) -> int:
            self.best = float('-inf')
            def gain(nd):
                if not nd:
                    return 0
                a = max(gain(nd.left), 0)
                b = max(gain(nd.right), 0)
                self.best = max(self.best, nd.val + a + b)
                return nd.val + max(a, b)
            gain(root)
            return self.best