n=int(input())
mat=[]
re=[]
for i in range(n):
    s=list(map(int,input().split(" ")))
    mat.append(s)
def row_col(mat1):
    
    smallnum=[100000]
    for i in range(0,len(mat1)):
        for j in range(0,len(mat1[i])):
            if((mat1[i].count(mat1[i][j]))>=4):
                smallnum.append(mat1[i][j])
    return(min(smallnum))
def transpose(mat1):
 
    l2 = list(map(list, zip(*mat1)))
    
    return l2
main=row_col(mat)
re.append(main)
main=row_col(transpose(mat))
re.append(main)

def daigg(mat1):
    temp=[]
    small=[100000]
    for  i in range(0,len(mat1)):
        temp.append(mat1[i][i])
    
    set1=list(set(temp))
    for i in set1:
        if(temp.count(i)>=4):
            small.append(i)
    return(min(small))
def secon_diag(mat1):
    temp=[]
    small=[100000]
    for  i in range(0,len(mat1)):
        temp.append(mat1[i][len(mat1)-i-1])
    
    set1=list(set(temp))
    for i in set1:
        if(temp.count(i)>=4):
            small.append(i)
    return(min(small))
main=daigg(mat)
re.append(main)
main=secon_diag(mat)
re.append(main)
re=list(set(re))        
if(len(re)==1):
    print(-1)
else:
    print(min(re))
           
    