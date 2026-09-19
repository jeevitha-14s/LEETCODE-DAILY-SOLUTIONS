class Solution:
        def diameterOfBinaryTree(self, root) -> int:
            self.best = 0
            def depth(nd):
                if not nd:
                    return 0
                a = depth(nd.left)
                b = depth(nd.right)
                self.best = max(self.best, a + b)
                return 1 + max(a, b)
            depth(root)
            return self.best