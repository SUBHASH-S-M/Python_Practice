num1=int(input("enter the 1st number "))
num2=int(input("enter the 2nd number "))
num1,num2=max(num1,num2),min(num1,num2)
hcf=1
for i in range(1,num2+1):
	if(num1%i==0 and num2%i==0):
		hfc=i
print(hcf)
	