s=list(map(int,input().split(",")))
from collections import Counter
re=[]
def printRepeating(arr, size):
    re=[]
 
    for i in range (0, size):
        for j in range (i + 1, size):
            if arr[i] == arr[j]:
                re.append(arr[i])
    return(re)
for i in range(len(s)):
    val=-355
    temp=[]
    temp.clear()
    temp=s[i+1:len(s)].copy()
    temp.sort()
    result=temp.copy()
    result = [item for items, c in Counter(temp).most_common()
                                 for item in [items] * c]
    
    
    if(len(result)!=len(set(result)) and len(result)!=0):
        
        val1=printRepeating(result,len(result)) 
        count=-1
        max1=-4500
        for j in val1:
            if(j>s[i]):
                count1=result.count(j)
                if(count1>count):
                    count=count1
                    max1=j
                elif(count1==count):
                    max1=min(max1,j)
        val=max1
        if(max1==-4500):
            val=-1
            
        
    else:
    
        for j in result:
            if(j>s[i]):
                val=j 
                break
            else:
                val=-1
    if(len(result)==0):
        val=-1
        
    re.append(val)
    result.clear()
re=list(map(str,re))
print(",".join(re))
        
 

           
        