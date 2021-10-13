input1=6
arr=[1,2,3]
for i in range(3,input1):
    arr.append(sum(arr[len(arr)-3:]))
return(arr[-1])