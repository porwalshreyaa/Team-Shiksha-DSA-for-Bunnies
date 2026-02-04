# Garima's Approach





# My failed attempts to come up with a solution


# strr= "bbaaacbd"
# def longestSubstring(s: str, k: int) -> int:
#     freq = {}
#     substring = ""
#     subsfre = {}
#     n = len(s)
#     for i in range(n):
#         if s[i] in freq.keys():
#             freq[s[i]]+=1
#         else:
#             freq[s[i]]=1
#     maxim=0
#     # print(freq)
#     for i in range(n):
#         substring+=s[i]
#         l = len(substring)
#         # print(l,s[i])
#         if freq[s[i]] < k:
#             l-=1
#             invalid=False
#             for p in range(l):
#                 if subsfre[s[p]]<k:
#                     invalid=True
#             if l>maxim and not invalid:
#                 maxim = l
#             substring = ""
#             subsfre={}
#             continue
#         if s[i] in subsfre.keys():
#             subsfre[s[i]]+=1
#         else:
#             subsfre[s[i]]=1
#     if l >maxim:
#         maxim=l
#     if maxim <k:
#         maxim = 0
#     return maxim

# print(longestSubstring(strr,3))
# # print(strr[:4])