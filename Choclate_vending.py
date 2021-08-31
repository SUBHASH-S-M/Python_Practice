# 1choclate cost = ₹1 and if i give 3 wrappers then ill get 1 choclate 
# cal(25,1,3)#25 ruppes , 1--> cost per choclate,3--> reimbursement rate 

def cal(amount_in_hand,price_per_chcolates,reimbusment_rate):
    remainng_wrappers=amount_in_hand//price_per_chcolates
    
    count=remainng_wrappers
    while(remainng_wrappers>=reimbusment_rate):
         count+=remainng_wrappers//reimbusment_rate 
         print("Count :",count)
         non_rem=remainng_wrappers%reimbusment_rate
         print("non_rem :",non_rem)
         remainng_wrappers=(remainng_wrappers//reimbusment_rate)+non_rem
         
         print("remainning_wrapper :",remainng_wrappers)
         non_rem=0
    return(count)

print(cal(25,1,3))
         
     