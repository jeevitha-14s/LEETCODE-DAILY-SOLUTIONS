class Solution:
        def isValidBST(self, root) -> bool:
            stack = [(root, float('-inf'), float('inf'))]
            while stack:
                nd, lo, hi = stack.pop()
                if not nd:
                    continue
                if not lo < nd.val < hi:
                    return False
                stack.append((nd.left, lo, nd.val))
                stack.append((nd.right, nd.val, hi))
            return True