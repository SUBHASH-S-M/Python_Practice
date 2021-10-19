def decodePacket(packetData):
    re=[]
    for i in range(0,len(packetData),8):
        re.append(packetData[i:i+8])
    
    b=re[0]
    temp=re[2:]
    if(len(temp)!=int(re[1],2)):
        return("Invalid packet")
    val=""
    for i in temp:
        temp1=int(re[1],2)
        temp2=int(i,2)
        t=temp1^temp2
        val+=chr(t)
    return val
        
        
print(decodePacket("00000111111110101111111111111111"))