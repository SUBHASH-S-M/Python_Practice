n=int(input())
symbol=input()
ele=[]
vow=['a','e','i','o','u','A','E','I','O','U']
for i in range(n):
    x=input()
    re=''
    for j in x:
        if(j in vow):
            re+=symbol
        else:
            re+=j
    ele.append(re)
for i in ele:
    print(i)
    
    
    
            