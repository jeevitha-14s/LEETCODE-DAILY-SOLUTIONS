class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def func(index, subset):
            res.append(subset[:])
            for i in range(index,len(nums)):
                if i>index and nums[i-1]==nums[i]:
                    continue
                subset.append(nums[i])
                func(i+1, subset)
                subset.pop()
        func(0,[])
        return res


        
        