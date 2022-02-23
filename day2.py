string=input()
n=int(input())
string='abcdefg'
n=2 
re=''
for i in range(0,len(string),n):
    re+=string[i:i+n]+' '
print(re)
    