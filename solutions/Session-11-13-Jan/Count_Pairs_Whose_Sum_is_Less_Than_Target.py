class Solution:
    def countPairs(self, arr, target):
        arr.sort()
        n=len(arr)
        i=0
        j=n-1
        count=0
        while i<j:
            if arr[i]+arr[j]>= target:
                j-=1
            else:
                count+=j-i
                i+=1
        return count