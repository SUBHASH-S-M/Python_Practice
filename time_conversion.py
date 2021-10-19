gmTime="0300"
zoneOffset="+0230"
re=""
if(zoneOffset[0]=="+"):
    flag=True
else:
    flag=False
for i in range(len(gmTime)):
    if(flag):
        re+=str(int(gmTime[i])+int(zoneOffset[i+1]))
       
    else:
        re+=str(int(gmTime[i])-int(zoneOffset[i+1]))
return(re)

    