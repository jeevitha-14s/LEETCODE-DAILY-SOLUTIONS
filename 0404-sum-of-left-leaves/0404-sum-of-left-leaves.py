class Solution:
        def sumOfLeftLeaves(self, root) -> int:
            total = 0
            stack = [root] if root else []
            while stack:
                nd = stack.pop()
                if nd.left:
                    if not nd.left.left and not nd.left.right:
                        total += nd.left.val
                    stack.append(nd.left)
                if nd.right:
                    stack.append(nd.right)
            return total