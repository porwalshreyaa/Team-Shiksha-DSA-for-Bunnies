class Solution:
    def getSecondLargest(self, arr):
        slargest=-1
        largest=arr[0]
        for i in arr:
            if i>largest:
                slargest = largest
                largest = i
            elif slargest<i<largest:
                slargest = i
        return slargest