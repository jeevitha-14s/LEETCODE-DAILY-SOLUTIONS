class Solution:
    def reverse(self, n: int) -> int:

        INT_MAX = 2**31 - 1

        revnum = 0

        if n < 0:
            sign = -1
        else:
            sign = 1

        n = abs(n)

        while n > 0:
            ld = n % 10
            n = n // 10

            # overflow check BEFORE updating revnum
            if revnum > INT_MAX // 10 or (revnum == INT_MAX // 10 and ld > 7):
                return 0

            revnum = (revnum * 10) + ld

        return sign * revnum