from collections import Counter
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counts = sorted(Counter(tasks).values())
        mx = counts[-1]
        same = counts.count(mx)
        return max(len(tasks), (mx - 1) * (n + 1) + same)