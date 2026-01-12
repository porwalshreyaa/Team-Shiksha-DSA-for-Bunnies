class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        sortedPointer = -1
        unsortedPointer = 0
        while unsortedPointer < length:
            if nums[unsortedPointer] !=0:
                nums[unsortedPointer], nums[sortedPointer+1] = nums[sortedPointer+1], nums[unsortedPointer]
                sortedPointer+= 1
            unsortedPointer+=1