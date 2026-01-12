class Solution:
    def leaders(self, arr):
        n = len(arr)
        maxElem = 0
        leaders = []
        for i in range(n-1,-1,-1):
            if arr[i]>=maxElem:
                maxElem = arr[i]
                leaders.append(maxElem)
        m = len(leaders)    
        for k in range(m//2):
            leaders[k],leaders[m-1-k]=leaders[m-1-k],leaders[k]
        return leaders