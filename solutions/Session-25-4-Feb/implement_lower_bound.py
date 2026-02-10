class Solution:
    def lowerBound(self, arr, target):
        low = 0
        high = len(arr)-1
        while low <=high:
            mid = (low+high)//2
            if arr[mid] < target:
                low = mid+1
                continue
            high = mid - 1
        return low