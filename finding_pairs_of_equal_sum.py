l=[34,89,6,321,53,45,2211,81]
from itertools import combinations
re=list(combinations(l,2))
count=0

def retsum(temp):
    return(sum(list(map(int,str(temp)))))
    
for i in re:
    m,n=i
    m=retsum(m)
    n=retsum(n)
    if(m==n):
        count+=1 
print(count)
    
    