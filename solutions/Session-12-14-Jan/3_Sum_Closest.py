class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        
        j=1
        i=0
        closest = float('inf')
        result=0
        while i<j:
            k=n-1
            j=i+1
            goal = target-nums[i]
            while j<k:
                currtwo=nums[j]+nums[k]

                if abs(goal-currtwo)<closest:
                    result=nums[i]+currtwo
                    closest=abs(goal-currtwo)
                if currtwo==goal:
                    return target
                elif currtwo<goal:
                    j+=1
                else:
                    k-=1
            i+=1
        return result