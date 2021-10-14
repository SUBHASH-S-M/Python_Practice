def solve(N,s):
    n=list(str(s))
    n=list(map(int,n))
    n.sort(reverse=True)
    n=list(map(str,n))
    return("".join(n))
    
    
    
print(solve(3,12))