'''
Write a python program to solve a classic ancient Chinese puzzle.

We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

'''




def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0

    #Start writing your code here
    #Populate the variables: chicken_count and rabbit_count
    if(legs%2!=0 or legs<2*(heads)):
        print(error_msg)
    else:
        if(heads*4==legs):
            rabbit_count=heads
        elif(heads*2==legs):
            chicken_count=heads
        else:
            rtally=(heads*4)-legs
            chicken_count=int(rtally/2)
            rabbit_count=heads-chicken_count
        print(chicken_count,rabbit_count)

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print(chicken_count,rabbit_count)
    #print(error_msg)

#Provide different values for heads and legs and test your program
solve(38,131)