from itertools import combinations
letters ="263589"
re=[]
result=[]
lenre=-1
for i in range(3,len(letters)+1):
    a = list(combinations(letters, i))
    re.append(a)
for i in range(0,len(re)):
    
    for j in range(0,len(re[i])):
        templist=list(re[i][j])
        templist=list(map(int,templist))
        
        flag=1
        for k in range(0,len(templist)-2):
            num1=templist[k]
            num2=templist[k+1]
            num3=templist[k+2]
            if(num3!=num2+num1):
                flag=0
            num1=num2
            num2=num3
        if(flag==1):
            if((len(result)<len(templist)) and lenre==-1):
                result.append(templist)
                lenre=0
                
            else:
                result.pop(-1)
                result.append(templist)
                
print(len(result[0]))
                
            
            
            
            
        
        
