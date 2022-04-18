n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
rate=int(input())
yrs=int(input())
def compound_interest(principle, rate, time):
    # Calculates compound interest
    Amount = principle * (pow((1 + rate / 100), time))
    CI = Amount - principle
    return CI
intrest=0
for i in arr:
    intrest+=compound_interest(i,rate,yrs)
print(int(intrest))