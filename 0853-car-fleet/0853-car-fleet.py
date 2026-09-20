class Solution:
        def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
            cars = sorted(zip(position, speed), reverse=True)
            fleets = 0
            slowest = 0.0
            for p, s in cars:
                t = (target - p) / s
                if t > slowest:
                    fleets += 1
                    slowest = t
            return fleets