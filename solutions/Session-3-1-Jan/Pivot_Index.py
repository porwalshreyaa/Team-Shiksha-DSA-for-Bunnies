class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tsum = 0
        for i in nums:
            tsum+=i
        rsum =0
        l = len(nums)
        for i in range(l):
            if rsum == tsum-rsum-nums[i]:
                return i
            rsum+=nums[i]
        return -1