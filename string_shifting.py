#  a string is given as input and an integer is also given ,we need to shift the string based on the number given if 2 is given as input shift 1st two char to last  


s=str(input())
k=int(input())
s=s[k:len(s)]+s[0:k]
print(s)
