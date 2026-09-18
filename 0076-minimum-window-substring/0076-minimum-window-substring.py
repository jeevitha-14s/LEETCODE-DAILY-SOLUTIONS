from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        left = 0
        res = ''
        for right, ch in enumerate(s):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1
            if missing:
                continue
            while need[s[left]] < 0:
                need[s[left]] += 1
                left += 1
            if not res or right - left + 1 < len(res):
                res = s[left:right + 1]
        return res