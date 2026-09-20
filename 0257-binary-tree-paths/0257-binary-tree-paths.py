class Solution:
        def binaryTreePaths(self, root) -> list[str]:
            res = []
            stack = [(root, str(root.val))]
            while stack:
                nd, path = stack.pop()
                if not nd.left and not nd.right:
                    res.append(path)
                if nd.left:
                    stack.append((nd.left, path + '->' + str(nd.left.val)))
                if nd.right:
                    stack.append((nd.right, path + '->' + str(nd.right.val)))
            return res