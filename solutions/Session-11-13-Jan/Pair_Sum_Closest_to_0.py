class Solution:
    def closestToZero (self,arr, n):
        arr.sort()
        currsum = 0
        summ = 0
        distance = 2000000
        i = 0
        j = n-1
        while i<j:
            currsum = arr[i]+arr[j]
            if distance > abs(currsum):
                distance = abs(currsum)
                summ = currsum
            if distance == abs(currsum) and summ<currsum:
                summ = currsum
            if currsum > 0:
                j-=1
            elif currsum <0:
                i+=1
            else:
                return summ
        return summ