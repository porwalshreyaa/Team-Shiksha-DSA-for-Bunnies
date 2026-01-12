class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        tsum= 0
        for num in nums:
            tsum+=num
        l = len(nums)
        leftSum = []
        rightSum = []
        answer = []
        rsum =0
        for i in range(l):
            leftSum.append(rsum)
            rsum +=nums[i]
            rightSum.append(tsum-rsum)
            v = leftSum[i] - rightSum[i]
            if v>=0:
                answer.append(v)
            else:
                answer.append((-v))
        return answer