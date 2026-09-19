import sys
sys.setrecursionlimit(10000)
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]):
        pos = {v: i for i, v in enumerate(inorder)}
        self.i = 0
        def build(lo, hi):
            if lo > hi:
                return None
            val = preorder[self.i]
            self.i += 1
            nd = TreeNode(val)
            mid = pos[val]
            nd.left = build(lo, mid - 1)
            nd.right = build(mid + 1, hi)
            return nd
        return build(0, len(inorder) - 1)