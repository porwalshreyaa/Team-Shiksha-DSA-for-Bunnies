class Solution:
    def sortColors(self, arr: List[int]) -> None:
        i=-1
        j=0
        n=len(arr)
        k=n-1
        while j<=k:
            if arr[j]==0:
                arr[j],arr[i+1]=arr[i+1],arr[j]
                i+=1
                j+=1
            elif arr[j]==2:
                arr[j],arr[k]=arr[k],arr[j]
                k-=1
            else:
                j+=1
        