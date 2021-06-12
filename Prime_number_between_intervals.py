def isprime(num):
	flag=True
	if(num<2):
		flag=False
	else:
		for i in range(2,(num)):
			if(num%i==0):
				flag=False
				break
	return(flag)
start_num=int(input("Enter the starting number"))
ending_num=int(input("Enter the ending number"))
for i in range(start_num,ending_num+1):
	if(isprime(i)):
		print(i)
