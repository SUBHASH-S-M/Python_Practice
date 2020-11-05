if __name__ == '__main__':
    n = int(input())
    arr = [57 ,57 ,-57 ,57]
    max1=-1000
    max2=-1000
    l=list(set(arr))
    sorted(l)
    for i in l:
        if(i>max1):
            max2=max1
            max1=i
        elif(i<max1 and i>max2):
            max2=i
        else:
            pass
    print(max2)