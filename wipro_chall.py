n=input()
even=0
odd=0
for i in n:
    if(int(i)%2==0):
        even+=int(i)
    else:
        odd+=int(i)
print(abs(even-odd))