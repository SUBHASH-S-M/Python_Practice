num=int(input())
flag=True
if(num<2):
	print("Prime number not defined")
else:
	for i in range(2,(num)):
		if(num%i==0):
			flag=False
			break
	if(flag==True):
		print("The number is a prime number")
	else:
		print("The number is not prime")