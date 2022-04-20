size=int(input())
n=int(input())
arr=[]
for i in range(n):
    val=list(map(int,input().split(" ")))
    if (val[0]==size and val[1]==size):
        print("ACCEPTED")
    elif(min(val)<size):
        print("UPLOAD ANOTHER")
    else:
        print("CROP IT")
