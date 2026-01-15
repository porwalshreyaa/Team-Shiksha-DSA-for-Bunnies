class Solution:
    def printClosest (self,arr, brr, n, m, x) : 
        i = 0
        j = m-1
        currsum = 0
        distance = 2000000000
        n1=-1
        n2=-2
        
        while i<n and j>=0:
            currsum = arr[i] + brr[j]
            if distance > abs(x-currsum):
                distance = abs(x - currsum)
                n1=arr[i]
                n2=brr[j]
            if currsum > x:
                j-=1
            else:
                i+=1
        return [n1,n2]