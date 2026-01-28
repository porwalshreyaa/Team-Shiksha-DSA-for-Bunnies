# With inbuilt strip method:-
class Solution:
    def reverseWords(self, s: str) -> str:
        rev = ""
        word = ""
        for i in s:
            if i != " ":
                word+=i
                continue
            if word:
                rev= " "+ word + rev
            word = ""
        rev = (word + rev).strip()
        return rev

# Without inbuilt strip method:-
class Solution:
    def reverseWords(self, s: str) -> str:
        rev = ""
        word = ""
        for i in s:
            if i != " ":
                word+=i
                continue
            if word:
                if rev != "":
                    rev= word + " "+ rev
                else:
                    rev= word + rev
                word = ""
        if rev=="":
            rev=word
        elif word:
            rev = (word + " "+ rev)
        return rev

print(reverseWords("  hello world  "))