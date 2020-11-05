per_com=[]
i=1 
j=1 
k=3
n=3
temp_list=[]
for i1 in range(0,i+1):
    for j1 in range(0,j+1):
        for k1 in range(0,k+1):
            
            temp_list.append([int(i1),int(j1),int(k1)])
            if(sum(temp_list[0])!=int(n) and len(temp_list[0])!=0):
                per_com.append(temp_list[0])
            
            temp_list.clear()

print(per_com)            