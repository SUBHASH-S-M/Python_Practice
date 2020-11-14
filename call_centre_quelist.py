
def func(k,arr):
    carry=0
    index=0
    for  i in range(0,len(arr)):
        diff=0
        if(arr[i]>k):
            carry=arr[i]-k
        if(arr[i]<k):
            diff=k-arr[i]
            carry=carry-diff
        index=i
        if(carry<=0 ):
            index=i
            return(i)
            break
    while(carry>0):
        carry=carry-k
        
        index=index+1
    return(index)
        
    
    
    
    
    
n=int(input())
for i in range(n):
    l=list(map(int,input().split(" ")))
    num_input=func(l[1],list(map(int,input().split(" "))))
    print(num_input+2)
# 2 
# 6 5 
# 10 5 5 3 2 1 
# 1 1
# 100
# 6
# 101

    