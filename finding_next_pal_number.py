num=int(input())
def ispali(temp):
    temp=str(temp)
    if(temp==temp[::-1]):
        return(True)
    else:
        return(False)


temp2=num
temp1=str(num)
while(1):
    
    temp2=int(temp1)+int(temp1[::-1])
    if(ispali(temp2)):
        print(temp2)
        break
    else:
        temp1=temp2
    temp1=str(temp1)
    
