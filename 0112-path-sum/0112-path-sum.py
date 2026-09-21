class Solution:
        def hasPathSum(self, root, targetSum: int) -> bool:
            stack = [(root, 0)] if root else []
            while stack:
                nd, acc = stack.pop()
                total = acc + nd.val
                if not nd.left and not nd.right and total == targetSum:
                    return True
                if nd.left:
                    stack.append((nd.left, total))
                if nd.right:
                    stack.append((nd.right, total))
            return False