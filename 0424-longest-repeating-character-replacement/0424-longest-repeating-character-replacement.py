class Solution:
        def characterReplacement(self, s: str, k: int) -> int:
            count = {}
            left = best = maxf = 0
            for right, ch in enumerate(s):
                count[ch] = count.get(ch, 0) + 1
                maxf = max(maxf, count[ch])
                while right - left + 1 - maxf > k:
                    count[s[left]] -= 1
                    left += 1
                best = max(best, right - left + 1)
            return best