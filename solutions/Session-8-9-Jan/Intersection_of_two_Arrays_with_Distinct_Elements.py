class Solution:
    def intersection(self, a, b):
        d = []
        i = 0
        j = 0
        
        while i< len(a) and j < len(b):
            if a[i] == b[j]:
                d.append(a[i])
                i+=1
                j+=1
            elif a[i]<b[j]:
                i+=1
            elif b[j]<a[i]:
                j+=1
        return d