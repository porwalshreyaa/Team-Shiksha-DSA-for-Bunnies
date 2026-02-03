class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = set()
        for i in nums:
            if i in d:
                return True
            else:
                d.add(i)
        return False

# Test case that fails[1000000000,1000000000,11] - Memory limit exceeded

# I was trying to design a simple set for this, I did not do hashing, lol!

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         max = 0
#         for i in nums:
#             if abs(i)>max:
#                 max = abs(i)
#         max+=1
#         d = [[0,0] for _ in range(max)]
#         for i in nums:
#             if i > 0:
#                 if d[i][0] ==0:
#                     d[i][0] = 1
#                 else:
#                     return True
#             else:
#                 k=abs(i)
#                 if d[k][1] == 0:
#                     d[k][1] = 1
#                 else:
#                     return True
#         return False