class Solution:
        def checkInclusion(self, s1: str, s2: str) -> bool:
            n, m = len(s1), len(s2)
            if n > m:
                return False
            need = [0] * 26
            win = [0] * 26
            for i, ch in enumerate(s1):
                need[ord(ch) - 97] += 1
                win[ord(s2[i]) - 97] += 1
            if need == win:
                return True
            for i in range(n, m):
                win[ord(s2[i]) - 97] += 1
                win[ord(s2[i - n]) - 97] -= 1
                if need == win:
                    return True
            return False