class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        res = []
        i=0
        j=0
        n=len(arr)
        k=0
        arr.sort()
        currsum=-1
        while i<n-2:
            j=i+1
            k=n-1
            while j<k:
                currsum = arr[i]+arr[j]+arr[k]
                if currsum>0:
                    k-=1
                elif currsum<0:
                    j+=1
                else:
                    res.append([arr[i],arr[j],arr[k]])
                    j+=1
                    k-=1
                    while j<k and arr[j]==arr[j-1]:
                        j+=1
                    while j<k and arr[k]==arr[k+1]:
                        k-=1
            i+=1
            while i<n-2 and arr[i]==arr[i-1]:
                i+=1
        return res