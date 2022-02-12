def getMaxUnit(num,boxes,unitSize,unitPerBox,truckSize):
    arr=[]
    for i in range(len(boxes)):
        temp=[boxes[i]]*unitPerBox[i]
        arr.extend(temp)
    arr.sort(reverse=True)
    count=0
    while(truckSize>0):
        m=max(arr)
        arr.remove(m)
        count+=m 
        truckSize-=1
    return count

print(getMaxUnit(3,[1,2,3],3,[3,2,1],3))