class Solution:
    def sumClosest(self, arr, target):
        arr.sort()
        
        n=len(arr)
        i=0
        j=n-1
        if n<2:
            return []
        res = []
        currsum=0
        distance=1000000
        diffofpair=-1
        while i<j:
            currsum=arr[i]+arr[j]
            currdist=abs(target-currsum)
            
            #best
            if distance > currdist:
                
                distance = currdist
                diffofpair=abs(arr[i]-arr[j])
                
                res = [arr[i],arr[j]]
                
            elif distance == currdist:
                
                if diffofpair < abs(arr[i]-arr[j]):
                    diffofpair = abs(arr[i]-arr[j])
                    
                    res = [arr[i],arr[j]]
            #move
            if currsum<target:
                i+=1
            else:
                j-=1
        res.sort()
        return res