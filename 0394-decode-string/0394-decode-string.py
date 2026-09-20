class Solution:
        def decodeString(self, s: str) -> str:
            stack = []
            cur = ''
            num = 0
            for ch in s:
                if ch.isdigit():
                    num = num * 10 + int(ch)
                    continue
                if ch == '[':
                    stack.append((cur, num))
                    cur = ''
                    num = 0
                    continue
                if ch == ']':
                    prev, cnt = stack.pop()
                    cur = prev + cur * cnt
                    continue
                cur += ch
            return cur