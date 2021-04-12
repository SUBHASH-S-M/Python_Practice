# Sample case 
# s="Abishek:34848,mayur:4739,friends:2949,yeah:9898"
# Sample Output
#             suex

s=input()

s="Abishek:34848,mayur:4739,friends:2949,yeah:9898"
s=list(s.split(","))

temp_list=[]
final_list=[]
def max1(l1,string):
    l1=list(map(int,l1))
    n1=len(string)
    lemg=[]
    for i in l1:
        if i <= n1:
            lemg.append(i)
    if(len((lemg))==0):
        return("")
    return(max(lemg))
            
for i in s:
    temp_list=i.split(":")
    x=max1(temp_list[1],temp_list[0])
    print(x)
    try: 
        final_list.append(temp_list[0][x-1])
    except:
        final_list.append("x")
print("".join(final_list))
        
    