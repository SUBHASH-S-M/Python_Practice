#Given a string get number from it and using the numbers form a largest even number and return it,
#if even number cannot be formed return -1.If no numbers present return -1.
#Priya@371 output: -1
#ranjithkumar@8421 output: 8412
#infyTQ output: -1




input_str=input("Enter the string : ")
input_str=list(input_str)
num=[]
for i in input_str:
    if(i.isdigit()):
        num.append(int(i))
num.sort(reverse=True)
flag=1
if(num!=[]):
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
            flag=-1
                
else:
    flag=-1
if(flag==1):            
    num=[str(i) for i in num]
    print("".join(num))
else:
    print(flag)