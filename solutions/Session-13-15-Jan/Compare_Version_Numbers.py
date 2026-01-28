def compareVersion(version1: str, version2: str) -> int:
    v1 = list(map(int, version1.split('.')))
    v2 = list(map(int, version2.split('.')))
    n=len(v1)
    m=len(v2)
    i=0
    while i < n and i <m:
        last1=v1[i]
        last2=v2[i]
        if v1[i]<v2[i]:
            return -1
        elif v1[i]>v2[i]:
            return 1
        i+=1
    while i<m:
        if v2[i]>0:
            return -1
        i+=1
    while i<n:
        if v1[i]>0:
            return 1
        i+=1
    return 0

print(compareVersion("1.0.0.2","1.0.0.2.7"))