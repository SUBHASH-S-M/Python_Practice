s=list(map(int,input().split(",")))

a=s[0:5]
b=s[5:10]
c=s[10:15]
d=s[15:20]
def cal_marks(i):
    return(a[i]+b[i]+c[i]+d[i])
marks=cal_marks(0)
print(marks)