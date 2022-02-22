n=int(input())
l=input().split(" ")
re=[]
for i in l:
    c=0
    for j in i:
        print(j)
        if(int(j)%2==0):
            c+=int(j)
    
    re.append(str(c))
print(" ".join(re))


    