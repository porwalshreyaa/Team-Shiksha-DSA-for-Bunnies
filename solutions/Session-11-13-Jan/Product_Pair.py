class Solution:
    def isProduct(self, arr, x):
        multiple = {}
        for i in arr:
            if x==0 and i ==0:
                return True
            if i!=0 and x%i ==0:
                compl=x//i
                if compl in multiple:
                    return True
                multiple[i] = 1
        return False