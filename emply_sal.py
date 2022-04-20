name=input()
arr=[]
val=0
for i in range(1,7):
    print("Day",i,":",end="")
    arr.append(float(input()))
for  i in arr:
    if(i>=8):
        val+=500
    elif(i>4 and i<8):
        val+=300
    elif(i<4 and sum(arr)>20):
        val+=100 
    elif (i<4 and sum(arr)<20):
        val+=50
    if(i>6):
        val+=15 
if(sum(arr)>32):
    val+=6*35 
print("Total Pay of {} is INR {}".format(name,val))


        
    
    