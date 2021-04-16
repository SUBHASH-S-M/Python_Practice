a="272"
res=[a[i:j] for  i in range(len(a)) for j in range(i+1,len(a)+1)]
res=list(set(map(int,res)))
def check_pronic(num):
    sqnum=int(num**0.5)
    if(num==sqnum*(sqnum+1)):
        return True
    else:
        return False
re=[]
for i in res:
    if(check_pronic(i)):
        re.append(i)
print(re)
        