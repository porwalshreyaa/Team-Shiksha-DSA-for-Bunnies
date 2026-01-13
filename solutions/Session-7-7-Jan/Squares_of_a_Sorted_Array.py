class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0
        right = n-1
        res=[0]*n
        pos =n-1
        while left<=right:
            if abs(nums[left])>abs(nums[right]):
                res[pos]=nums[left]*nums[left]
                left+=1
            else:
                res[pos]=nums[right]*nums[right]
                right-=1
            pos-=1
        return res