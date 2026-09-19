class Solution:
        def isSubtree(self, root, subRoot) -> bool:
            def same(a, b):
                if not a or not b:
                    return a is b
                return a.val == b.val and same(a.left, b.left) and same(a.right, b.right)
            stack = [root]
            while stack:
                nd = stack.pop()
                if not nd:
                    continue
                if same(nd, subRoot):
                    return True
                stack.append(nd.left)
                stack.append(nd.right)
            return False