import re
string="ababcs73119755dsds"
str1=re.findall('[0-9]',string)
str1=list(set(map(int,str1)))

even=[]
flag=1
for i in str1:
    if(i%2==0):
        even.append(i)

if(len(even)==0):
    print("-1")
else:
    minval=min(even)
    str1.remove(minval)
    str1.sort(reverse=True)
    str1.append(minval)
    str1=list(map(str,str1))
    str1="".join(str1)
    print(str1)


    