class Solution:
    def rev(self, nums:List[int], start, end) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start] 
            start +=1
            end -=1
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k%=len(nums)
        self.rev(nums, 0, len(nums)-k-1)
        self.rev(nums, len(nums)-k, len(nums)-1)
        self.rev(nums,0,len(nums)-1)