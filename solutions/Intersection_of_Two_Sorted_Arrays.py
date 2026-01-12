class Solution:
    def intersection(self, arr1, arr2):
        a =0
        b =0
        alen=len(arr1)
        blen=len(arr2)
        maxum=0
        intersect = []
        while a<alen and b<blen:
            if arr1[a]==arr2[b]:
                if maxum!=arr1[a]:
                    maxum = arr1[a]
                    intersect.append(maxum)
                a+=1
                b+=1
            else:
                if arr1[a]<arr2[b]:
                    a+=1
                else:
                    b+=1
        return  intersect