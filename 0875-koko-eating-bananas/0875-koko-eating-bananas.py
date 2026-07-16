class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n=len(piles)
        low=1
        high=max(piles)
        #ans=float('inf')
        while low<=high:
            mid=(low+high)//2
            total=0
            for pile in piles:
                total= total+ (pile+mid-1)//mid

            if total<=h:
                ans=mid
                high=mid-1

            else:
                low=mid+1

        return ans



        