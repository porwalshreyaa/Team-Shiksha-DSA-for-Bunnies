class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        value = None
        count = 0
        for i in nums:
            if value:
                if value !=i:
                    count -=1
                    if count ==0:
                        value=None
                else:
                    count+=1
            else:
                value=i
                count=1
        return value