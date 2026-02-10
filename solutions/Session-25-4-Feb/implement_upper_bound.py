class Solution:
    def upperBound(self, arr, target):
        low = 0
        high =len(arr)-1
        while low <=high:
            mid = (low+high)//2
            if target < arr[mid]:
                high = mid-1
                continue
            low = mid+1
        return low