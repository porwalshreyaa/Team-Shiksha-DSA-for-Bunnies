class Solution:
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        na = len(a)
        nb = len(b)
        res=[]
        i=0
        j=0
        while i<na and j<nb:
            if a[i]<b[j]:
                res.append(a[i])
                i+=1
            elif a[i]>b[j]:
                res.append(b[j])
                j+=1
            else:
                res.append(b[j])
                j+=1
                i+=1
        while i<na:
            res.append(a[i])
            i+=1
            
        while j<nb:
            res.append(b[j])
            j+=1
        return res