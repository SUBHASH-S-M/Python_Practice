string="ru"
flag=False
#RUN whether u is after r and before n
for i in range(len(string)):
	if(string[i]=='r'):
		for j in range(i+1,len(string)):
			if(string[j]=='u'):
				for k in range(j+1,len(string)):
				    if(string[k]=='n'):
					    flag=True
print(flag)