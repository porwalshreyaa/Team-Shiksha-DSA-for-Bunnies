class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxim = -1
        n =len(arr)
        for i in range(n-1,-1,-1):
            if arr[i]<maxim:
                arr[i]=maxim
            else:
                temp = maxim
                maxim = arr[i]
                arr[i] = temp
        arr[-1] =-1
        return arr