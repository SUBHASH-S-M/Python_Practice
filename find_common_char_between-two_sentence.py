'''
Write a python program to display all the common characters between two strings. Return -1 if there are no matching characters.

Note: Ignore blank spaces if there are any. Perform case sensitive string comparison wherever necessary.
'''
#PF-Assgn-33

def find_common_characters(msg1,msg2):
    l=[]
    for i in msg1:
         if(i in msg2 and i not in l):
             l.append(i)
    if(" " in l):
        l.remove(" ")
   
    if(len(l)>0):
        return("".join(l))
    else:
        return(-1)
#Provide different values for msg1,msg2 and test your program
msg1="Moto"
msg2="Apple"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)