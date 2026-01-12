class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        j = 2
        n = len(nums)
        while j<n:
            if nums[i]==nums[j] and nums[i-1]==nums[j]:
                j+=1
            else:
                nums[i+1]=nums[j]
                i+=1
                j+=1
        return i+1