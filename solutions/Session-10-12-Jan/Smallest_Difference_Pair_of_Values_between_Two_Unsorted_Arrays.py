# A = [1, 2, 11, 5]
# B = [4, 12, 19, 23, 127, 235]

# Answer Expected: 1

# A = [1, 3, 15, 11, 2]
# B = [23, 127, 235, 19, 8]

# Answer Expected: 3

# A = [10, 5, 40]
# B = [50, 90, 80]

# Answer Expected: 10

def findSmallestDiff(a:list,b:list) -> int:
    a.sort() # O(mlog(m))
    b.sort() # O(nlog(n))

    m = len(a)
    n = len(b)

    i = 0
    j = 0

    minimum = abs(a[0]-b[0])
    while i<m and j<n:
        diff = abs(a[i]-b[j])
        if diff < minimum:
            minimum=diff
        if a[i]<b[j]:
            i+=1
        else:
            j+=1
    return minimum

# print(findSmallestDiff(A,B))