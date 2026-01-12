# class Solution:
#     def leftRightDifference(self, nums: List[int]) -> List[int]:
#         tsum= 0
#         for num in nums:
#             tsum+=num
#         l = len(nums)
#         leftSum = []
#         rightSum = []
#         answer = []
#         lsum =0
#         for i in range(l):
#             leftSum.append(lsum)
#             lsum +=nums[i]
#             rightSum.append(tsum-lsum)
#             v = leftSum[i] - rightSum[i]
#             if v>=0:
#                 answer.append(v)
#             else:
#                 answer.append((-v))
#         return answer


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        tsum= 0
        for num in nums:
            tsum+=num
        l = len(nums)

        answer = []
        lsum =0
        rsum=0
        for i in range(l):
            rsum =tsum-nums[i]-lsum
            v = lsum - rsum
            lsum+=nums[i]
            if v>=0:
                answer.append(v)
            else:
                answer.append((-v))
        return answer