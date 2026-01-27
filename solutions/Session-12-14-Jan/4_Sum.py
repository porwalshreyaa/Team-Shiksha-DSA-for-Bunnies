class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        i=0
        j=i+1
        result=[]
        while i<n-3:
            j=i+1
            while j<n-2:
                sumij=nums[i]+nums[j]
                target2=target-sumij
                k=j+1
                l=n-1
                while k<l:
                    curr2=nums[k]+nums[l]
                    if curr2==target2:
                        rightset= [nums[i], nums[j], nums[k], nums[l]]
                        result.append(rightset)
                        k+=1
                        while nums[k-1]==nums[k] and k<l:
                            k+=1
                    elif curr2<target2:
                        k+=1
                        while nums[k-1]==nums[k] and k<l:
                            k+=1
                    else:
                        l-=1
                        while nums[l]==nums[l+1] and l>i+3:
                            l-=1
                    
                j+=1
                while nums[j-1]==nums[j] and j<n-2:
                    j+=1
                
            i+=1
            while nums[i-1]==nums[i] and i<n-3:
                i+=1
        return result