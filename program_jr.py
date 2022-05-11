
def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True
def palindrom(n):
    if(n==n[::-1]):
        return True
    return False 
arr=[]
for i in range(int(input())):
    val=list(map(int,input().split(" ")))
    arr.append(val)
count=0
for j in arr:
    for i in range(j[0],j[1]+1):
        if(isprime(i) and palindrom(str(i))):
            count+=1
print(count)