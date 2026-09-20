class Solution:
        def sortedArrayToBST(self, nums: list[int]):
            def build(lo, hi):
                if lo > hi:
                    return None
                mid = (lo + hi) // 2
                nd = TreeNode(nums[mid])
                nd.left = build(lo, mid - 1)
                nd.right = build(mid + 1, hi)
                return nd
            return build(0, len(nums) - 1)