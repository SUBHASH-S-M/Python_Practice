 #Generate a password from the given N set of String and digits separated by colon(:)
#and each set is separated by comma with following conditions
#Find the largest digit X smaller than or equal length of the string and choose the character
#in the string at position X assuming that index starting from 1.
#if there is no such digit exsits place X (Capital X) instead.
# Ranjith:67543,Priya:374,Kumar:210,passion:89
# hyuX



def str_to_int(l):
    for i in range(len(l)):
        l[i]=int(l[i])
    return(l)
        
def password(l):
    name=l[0]
    cahr=[]
    numbers=str_to_int(list(l[1]))
    len_name=len(name)
    while len(cahr)==0:
        
        if(len_name in numbers):
            cahr.append(name[len_name-1])
        len_name-=1
        if(len_name==0):
            cahr.append("X")
            break
    return(cahr)    
    
    
s="Ranjith:67543,Priya:374,Kumar:210,passion:89"
a=[]
name=s.split(",")
for i in name:
    a.extend(password(i.split(':')))
print(''.join(a))
    