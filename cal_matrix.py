def sumOfAll(n,A,p,q):
    val=0
    r=len(A)
    c=len(A[0])
    if(p-1<r and q-1<c):
        val+=A[p-1][q-1]
       
    if(p-1<r and q<c):
        val+=A[p-1][q]
        

    if(p-1<r and q+1<c):
        val+=A[p-1][q+1]
       
        
    if(p<r and q-1<c):
        val+=A[p][q-1]
       
    if(p<r and q+1<c):
        val+=A[p][q+1]
        
    if(p+1<r and q-1<c):
        val+=A[p+1][q-1]
       
    if(p+1<r and q<c):
        val+=A[p+1][q]
       
    if(p+1<r and q+1<c):
        val+=A[p+1][q+1]
        
    return(val)
    
A=[[11,22,33],[44,55,66],[77,88,99]]
n=4 
p=1
q=1
print(sumOfAll(n,A,p,q))


