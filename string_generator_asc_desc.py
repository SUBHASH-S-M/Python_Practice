import math as mt
s="HeLloOWorLDd"
small_s=s.lower()
temp_re=[]
final_st=""
small_s=list(set(small_s))
for i in small_s:
    temp_str=""
    for j in range(len(s)):
        if(s[j]==i.lower() or s[j]==i.upper()):
            temp_str=temp_str+s[j]
    temp_re.append(temp_str)
temp_re.sort(key=str.lower)
middle=mt.floor(len(temp_re)/2)
asc_g=temp_re[0:middle]
desc_g=temp_re[middle:len(temp_re)]
desc_g.reverse()


for i in range(len(asc_g)):
    final_st=final_st+asc_g[i]
    final_st=final_st+desc_g[i]
if(len(s)//2==0):
    print(final_st)
else:
    final_st=final_st+desc_g[-1]
    print(final_st)
    