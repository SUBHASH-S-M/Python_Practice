# vowel virus decoder
s="weird"
re=""
for i in s:
    if(i in ['a','e','i','o','u']):
        re+='x'*(ord(i)-96)
    else:
        re+=i 
print(re)

