class Solution:
    def allPairs(self, target, arr1, arr2):
        arr1.sort()
        s = {}
        for i in arr2:
            s[i] = s.get(i, 0) +1
        comp = 0
        res =[]
        for i in arr1:
            comp = target - i
            if comp in s:
                res.extend([(i, comp)]*s[comp])
        return res