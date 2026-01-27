def majorityElement(nums):
    n=len(nums)
    value1=None
    value2=None
    counter1=0
    counter2=0
    for i in nums:
        if value1 is not None and value2 is not None:
            if value1==i:
                counter1+=1
            elif value2==i:
                counter2+=1
            else:
                counter1-=1
                counter2-=1
                if counter1==0:
                    value1=None
                if counter2==0:
                    value2=None
        elif value1 is None and value2 is None:
                value1=i
                counter1=1
        elif value1 is None:
            if value2==i:
                counter2+=1
            else:
                value1=i
                counter1=1
        elif value2 is None:
            if value1==i:
                counter1+=1
            else:
                value2=i
                counter2=1

    max1=0
    max2=0
    for i in nums:
        if value1 is not None:
            if i==value1:
                max1+=1
        if value2 is not None:
            if i==value2:
                max2+=1
    res=[]
    if max1>n//3:
        res.append(value1)
    if max2>n//3:
        res.append(value2)
    return res

print(majorityElement([1,2]))