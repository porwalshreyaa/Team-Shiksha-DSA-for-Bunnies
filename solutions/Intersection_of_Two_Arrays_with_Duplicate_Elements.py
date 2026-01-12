class Solution:
    def intersect(self, a, b):
        d={}
        for i in a:
            d[i] = 1
        for i in b:
            if i in d.keys():
                d[i] = 2
        f = []
        for i in d.keys():
            if d[i]==2:
                f.append(i)
        return f