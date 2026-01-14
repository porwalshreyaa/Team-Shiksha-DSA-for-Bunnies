class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        keymap = {}
        n = len(numbers)
        for i in range(n):
            comp = target - numbers[i]
            if comp in keymap.keys():
                if keymap[comp] != i:
                    return [keymap[comp]+1, i+1]
            keymap[numbers[i]] =i

# Sorted property not used... 
# 
# there is a better approach using two pointers from opposite ends

class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        n = len(num)
        i = 0
        j = n-1
        while i<j:
            cur_sum = num[i] + num[j]
            if cur_sum == target:
                return [i+1, j+1]
            if cur_sum < target:
                i+=1
            else:
                j-=1