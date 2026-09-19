class Solution:
        def letterCombinations(self, digits: str) -> list[str]:
            if not digits:
                return []
            pad = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
            res = ['']
            for d in digits:
                res = [p + ch for p in res for ch in pad[d]]
            return res