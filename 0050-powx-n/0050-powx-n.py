class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def pow(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            
            if n % 2 == 0:
                return pow(x * x, n // 2)
            else:
                half = pow(x, n // 2)
                return half * half * x
        
        if n < 0:
            return 1 / pow(x, -n)

        return pow(x, n)