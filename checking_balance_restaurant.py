
'''
CODING. MAFIA 
Asked in Coding Interviews Difficulty level : hard 
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer, so that the net transaction is that the customer pays $5. Note that you don't have any change in hand at first. Return true if and only if you can provide every customer with correct change. 
Input : [5,5,5,10,20] Output : true 

'''

array=[5,5,5,5,10,20]
bank_deno=0
flag=True
for i in array:
    if(i==5):
        bank_deno+=1
        
        
    else:
        
        if(int((i-5)/5)<=bank_deno):
            
            bank_deno-=int(((i-5)/5))
            
            
        else:
            flag=False
print(flag)