def isPalindrome(s: str) -> bool:
    s=s.lower()
    i=0
    j=len(s)-1
    while i<=j:
        if (not s[i].isalnum())or s[i]==" ":
            i+=1
            continue
        if (not s[j].isalnum()) or s[j]==" ":
            j-=1
            continue
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))