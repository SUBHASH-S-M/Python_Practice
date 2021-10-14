def solve(n,k,str1,str2):
    str1=list(str1)
    str2=list(str2)
    a=[]
    a.extend(str1)
    a.extend(str2)
    a=list(set(a))
    count=0
    for i in a:
        if(str1.count(i)==str2.count(i)):
            count+=str1.count(i)
    return(count)
    
    
print(solve(1,2,"aba","aabfc"))