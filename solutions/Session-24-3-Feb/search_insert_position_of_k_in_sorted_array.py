class Solution:
    def searchInsertK(self, arr, k):
        n=len(arr)
        l = 0
        r = n-1
        while l<=r:
            mid = int(l + (r-l)/2)
            if arr[mid] == k:
                return mid
            elif arr[mid]<k:
                l = mid+1
            elif arr[mid]>k:
                r = mid-1
        if k < arr[mid]:
            return mid
        else:
            return mid+1

# Think about what could have been it's position without replacing another element (shifting is valid)