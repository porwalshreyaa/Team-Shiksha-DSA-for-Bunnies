# Brute force - O(n^2)
def brute(arr:list,target:int)->int:
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if target == arr[i] + arr[j]:
                count+=1
    return count

# Better - O(nlog(n))
def twopointer(arr:list,target:int)->int:
    n = len(arr)
    count = 0
    i = 0
    j = n-1
    arr.sort() # this takes O(nlog(n))
    while i<j:
        total=arr[i]+arr[j]
        if total<target:
            i+=1
        elif total>target:
            j-=1
        else:
            count_n1 = 0
            count_n2 = 0
            n1 = arr[i]
            n2 = arr[j]
            while i<=j and arr[i]==n1:
                count_n1+=1
                i+=1
            while i<=j and arr[j]==n2:
                count_n2+=1
                j-=1
            if n1 == n2:
                # first element would have n-1 combinations and so on...
                # sum of k natural numbers where k is n-1 here k*(k+1)//2 = (n-1)*n//2
                count+= count_n1*(count_n1-1)//2
            else:
                count+=count_n1* count_n2
    return count

# Optimized - O(n)

class Solution:
    def countPairs(self, arr, target):
        d = {}
        count = 0
        for i in arr:
            if target-i in d:
                count += d[target-i]
            d[i] = d.get(i,0) + 1
        return count