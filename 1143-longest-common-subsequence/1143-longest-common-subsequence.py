class Solution:
        def longestCommonSubsequence(self, text1: str, text2: str) -> int:
            n = len(text2)
            prev = [0] * (n + 1)
            for a in text1:
                cur = [0] * (n + 1)
                for j in range(n):
                    cur[j + 1] = prev[j] + 1 if a == text2[j] else max(prev[j + 1], cur[j])
                prev = cur
            return prev[n]