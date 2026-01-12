class Solution:
    def reverseArray(self, arr):
        j = len(arr)-1
        i = 0
        while i<j:
            arr[i],arr[j]=arr[j],arr[i]
            j-=1
            i+=1
        return  arr