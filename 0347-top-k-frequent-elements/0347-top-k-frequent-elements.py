from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for x, c in count.items():
            buckets[c].append(x)
        res = []
        for c in range(len(nums), 0, -1):
            for x in buckets[c]:
                res.append(x)
                if len(res) == k:
                    return res
        return res