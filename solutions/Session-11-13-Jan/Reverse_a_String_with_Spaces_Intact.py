class Solution:
    def reverseWithSpacesIntact(self, s):
        n = len(s)
        i=0
        j=n-1
        fs = ""
        bs = ""
        while i<j:
            if s[i]!=" " and s[j]!= " ":
                fs+=s[j]
                bs=s[i]+bs
                i+=1
                j-=1
            elif s[i] == " ":
                fs+= " "
                i+=1
            elif s[j] == " ":
                bs = " "+bs
                j-=1
        if i==j:
            fs+= s[i]
        return fs+bs