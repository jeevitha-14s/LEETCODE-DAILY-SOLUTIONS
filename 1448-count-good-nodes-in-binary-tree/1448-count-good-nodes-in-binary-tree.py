class Solution:
        def goodNodes(self, root) -> int:
            count = 0
            stack = [(root, root.val)]
            while stack:
                nd, best = stack.pop()
                if nd.val >= best:
                    count += 1
                nb = max(best, nd.val)
                if nd.left:
                    stack.append((nd.left, nb))
                if nd.right:
                    stack.append((nd.right, nb))
            return count