r1=int(input())
r2=int(input())


mat1=[]
mat2=[]
re1=[]
nmat2=[]
for i in range(r1):
    mat1.append(list(map(int,input().split(" "))))
for i in range(r2):
    mat2.append(list(map(int,input().split(" "))))

c1=len(mat1[0])
c2=len(mat2[0])

nmat2=[mat2[i][j] for i in range(r2) for j in range(c2)]
re=[]
for i in range(r1):
    for j in range(c1):
        
        num=-100
        temp=[]
        temp.clear()
        try:
            num=mat1[i][j]*mat2[i][j]
            temp.append(num)
        except IndexError :
            num=-1
            temp.append(-1)
        try:
            num=mat1[i][j]*mat2[j][i]
            temp.append(num)
        except IndexError :
            num=-1
            temp.append(-1)
        try:
            num=mat1[i][j]*mat2[i][i]
            temp.append(num)
        except IndexError :
            num=-1
            temp.append(-1)
        try:
            num=mat1[i][j]*mat2[j][j]
            temp.append(num)
        except IndexError :
            num=-1
            temp.append(-1)
        if(len(set(temp))!=1 and temp.count(-1)>0):
            while(temp.count(-1)>0 and len(temp)>1):
                x=temp.index(-1)
                temp.pop(x)
        
        print(min(temp),end=" ")
    print()
        
    
    
#re=list(map(str,re))

#print(re)

    
        
            


    