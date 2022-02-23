n1=int(input())
n2=int(input())
c=0
for i in range(n1+1,n2):
    if(i**0.5==int(i**0.5)):
        c+=i 
print(c)


