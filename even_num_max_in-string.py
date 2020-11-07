s="sd8421"
s=list(s)
num=[]
for i in s:
    if(i.isdigit()):
        num.append(int(i))
num.sort(reverse=True)
if(num[-1]%2==0):
    pass
else:
    for i in range(len(num)-1,-1,-1):
        pos=1000
        if (num[i]%2==0):
            pos=i
            temp=num[i]
            num.pop(i)
            num.append(temp)
            break
            
    else:
        print("-1")
        
num=[str(i) for i in num]
print("".join(num))