class Solution:
        def lemonadeChange(self, bills: list[int]) -> bool:
            five = ten = 0
            for b in bills:
                if b == 5:
                    five += 1
                if b == 10:
                    five, ten = five - 1, ten + 1
                if b == 20:
                    five, ten = (five - 1, ten - 1) if ten else (five - 3, ten)
                if five < 0:
                    return False
            return True