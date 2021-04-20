# cook your dish here
s=input()

re=[s[i:j] for i in range(0,len(s)) for j in range(i+1,len(s)+1)]
for i in re:
    
    if(len(i)%2!=0 and len(i)==1  ):
        re.remove(i)
ref=[]
for  i in set(re):
    
    flag=1
    str1=list(map(str,i))
    count1=str1.count(str1[0])
    for j in set(str1):
        count2=str1.count(j)
        if(count1==count2):
            pass
        else:
            flag=0
            break
    if(flag==1):
        ref.append(i)
ref.sort(key=str.lower)
ref.sort(key=len)
re1=[]
for i in ref:
    
    str1=list(map(str,i))
    
    if(len(str1)==len(list(set(str1)))):
        pass
    else:
        re1.append(i)
print(",".join(re1))
        
    