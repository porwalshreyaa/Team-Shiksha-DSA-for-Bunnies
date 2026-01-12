class Solution:
    def intersectSize(self,a, b):
        d={}
        for i in a:
            d[i] = 1
        for i in b:
            if i in d.keys():
                d[i] = 2
        count = 0
        for i in d.keys():
            if d[i]>1:
                count+=1
                
        return count