def solver1(s:list[str])->None:
    s[:]=s[::-1]
def solver2(s:list[str])->None:
    l, r = 0,len(s)-1
    while l>r:
        s[l],s[r]=s[r],s[l]
        l+=1
        r-=1
s=input()
solver1(s)
solver2(s)
