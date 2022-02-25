arr=list(map(int,input().split(" ")))
n=arr[0]
goods=arr[1]
re=[]
for i in range(1,n+1):
    re.append(goods%i)
print(max(re)) 

  