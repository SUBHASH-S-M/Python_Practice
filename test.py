vowels=['a','e','i','o','u']
vowelsc=['A','E','I','O','U']
inp=input()
re=''
for i in inp:
    if(i=='u' or i=='U'):
        if(i=='u'):
            re+=vowels[0]
        else:
            re+=vowelsc[0]
    elif(i in vowels or i in vowelsc):
        if(i in vowels):
            re+=vowels[vowels.index(i)+1]
        else:
            re+=vowelsc[vowelsc.index(i)+1]
    else:
        re+=i 
print(re)
            
    
        
        