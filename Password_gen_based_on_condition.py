s="4365188"
re=""
for i in range(1,len(s),2):
    re=re+s[i] 
print(re)
re=[str(int(i)**2) for i in re]
re="".join(re)
print(re[0:4])
    