class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexset = {}
        n = len(nums)
        for i in range(n):
            val = target - nums[i]
            if val in indexset.keys():
                return [indexset[val],i]
            indexset[nums[i]]=i
        return -1