def find_leap_years(given_year):
    count=0
    curry=given_year
    list_of_leap_years=[]
    
    while(count<15):
        curry+=1
        
        if((curry%4==0 and curry%100!=0) or curry%400==0):
            list_of_leap_years.append(curry)
            count+=1
            
    print(list_of_leap_years)
        


find_leap_years(1996)