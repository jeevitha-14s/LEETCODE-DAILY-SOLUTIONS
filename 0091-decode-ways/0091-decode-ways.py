class Solution:
        def numDecodings(self, s: str) -> int:
            a, b = 1, int(s[0] != '0')
            for i in range(1, len(s)):
                c = b if s[i] != '0' else 0
                if s[i - 1] != '0' and int(s[i - 1:i + 1]) <= 26:
                    c += a
                a, b = b, c
            return b