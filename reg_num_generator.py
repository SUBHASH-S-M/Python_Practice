n=input()
re=[]
for i in range(0,len(n)-1,2):
    n1=int(n[i])
    n2=int(n[i+1])
    re.append(str(max(n1,n2)))
if(len(n)%2!=0):
    re.append(n[-1])
print("".join(re))
