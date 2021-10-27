n=input()
re=[]
for i in range(n):
    re.append(int(input()))

for i in range(n):
    for j in range(n):
        
        if(i!=j and re[i]<re[j]):
            if(j-i>=mx):
                mx=j-i
print(mx)
        
        