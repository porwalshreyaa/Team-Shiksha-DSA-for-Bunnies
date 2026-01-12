class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        n = len(nums)
        while j<n:
            if nums[i] != nums[j]:
                nums[i+1]= nums[j]
                i+=1
            j+=1
        return i+1