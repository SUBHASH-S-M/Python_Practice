bhk=[4,6,1,3,3,4,5]
op=[12,10,12,15,19,10,16]
sum1=0 
t1=0 
t2=0 

for i in range(len(bhk)):
    t1+=(bhk[i]-3.71)**2
    t2+=(op[i]-13.42)**2
    
print(t1,t2)