class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        if n<2:
            return 
        if n<=2:
            nums[0],nums[1]=nums[1],nums[0]
            return
        i = n-2
        while i>=0 and nums[i]>= nums[i+1]:
            i-=1
        if nums[i]<nums[i+1]:
            pivot = i
        if pivot !=-1:
            k=n-1
            while k>=0 and nums[k]<=nums[pivot]:
                k-=1
            if nums[k]>nums[pivot]:
                nums[k],nums[pivot]=nums[pivot],nums[k]
        i=pivot+1
        j=n-1
        while i<j:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
        return