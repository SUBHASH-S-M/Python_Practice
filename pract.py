#factorial
input_num=5
fact=1 
for i in range(1,input_num+1):
    fact=fact*i
#print(fact)

#gcd
inp_num1=54
inp_num2=10
inp_num1,inp_num2=min(inp_num1,inp_num2),max(inp_num1,inp_num2)
#print(inp_num1,inp_num2)
for i in range(1,inp_num1+1):
    if(inp_num1%i==0 and inp_num2%i==0):
        gcd=i
#print(gcd)

#prime
num=1
Flag=True
for i in range(2,num):
    if(num%i==0):
        Flag=False 
if(Flag or num==1):
    print("Prime")
else:
    print("Not Prime")
    
#amstrong
num=153
sum=0
for i in str(num):
    sum+=int(i)**len(str(num))
if(sum==num):
    print("Amstrong")
else:
    print("Not Amstrong")

#fibonaci
n=int(input())
seeds=[0,1]
if(n>0 and n<2):
    print(seeds[:n])
else:
    for i in range(2,n):
        seeds.append(sum(seeds[len(seeds)-2:]))
print(seeds)