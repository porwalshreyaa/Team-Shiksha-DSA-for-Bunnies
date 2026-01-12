class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l = len(nums)
        rsum=0
        for i in range(l):
            rsum += nums[i]
            nums[i] = rsum
        
        return nums