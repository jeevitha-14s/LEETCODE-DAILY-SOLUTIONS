from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        s = [str(x) for x in nums]
        s.sort(key=cmp_to_key(lambda a, b: -1 if a + b > b + a else 1))
        res = ''.join(s)
        return '0' if res[0] == '0' else res