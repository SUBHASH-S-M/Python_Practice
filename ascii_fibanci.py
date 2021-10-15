input1="MORE"
d=['a','b']
n=[0,1]
for i in range(99,123):
    d.append(chr(i))
    n.append(sum(n[i-99:i-99+3]))
su1=0
for i in input1:
    s=i.lower()
    index=d.index(s)
    su1+=n[index]
print(su1)    
    

    
    
    