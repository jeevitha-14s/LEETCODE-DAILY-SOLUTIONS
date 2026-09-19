class Solution:
        def findDuplicate(self, nums: list[int]) -> int:
            slow = fast = 0
            while True:
                slow = nums[slow]
                fast = nums[nums[fast]]
                if slow == fast:
                    break
            other = 0
            while other != slow:
                other = nums[other]
                slow = nums[slow]
            return slow