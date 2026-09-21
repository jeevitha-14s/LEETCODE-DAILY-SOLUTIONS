class Solution:
        def isSymmetric(self, root) -> bool:
            stack = [(root.left, root.right)]
            while stack:
                a, b = stack.pop()
                if not a and not b:
                    continue
                if not a or not b or a.val != b.val:
                    return False
                stack.append((a.left, b.right))
                stack.append((a.right, b.left))
            return True