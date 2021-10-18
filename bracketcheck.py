s="(dfd{}"
po_c=0
pc_c=0
fo_c=0
fc_c=0
for i in s:
    if(i=='('):
        po_c+=1 
    elif(i==')'):
        pc_c+=1 
    elif(i=='{'):
        fo_c+=1 
    elif(i=='}'):
        fc_c+=1 
flag=True
if(po_c!=pc_c):
    flag=False
if(fc_c!=fo_c):
    flag=False 
if(flag):
    print("correct")
else:
    print("error")
    