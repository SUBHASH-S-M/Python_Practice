'''
Write a python program which finds the maximum number from num1 to num2 (num2 inclusive) based on the following rules.

Always num1 should be less than num2
Consider each number from num1 to num2 (num2 inclusive). Populate the number into a list, if the below conditions are satisfied
Sum of the digits of the number is a multiple of 3
Number has only two digits
Number is a multiple of 5
Display the maximum element from the list
In case of any invalid data or if the list is empty, display -1.
'''

def find_max(num1, num2):
    max_num=-1
    # Write your logic here
    max_valid=[]
    initial=num1
    while(num1<=num2 and num1<100):
        temp=list(str(num1))
        temp=map(int,temp)
        if(sum(temp)%3==0 and num1%5==0):
            max_valid.append(num1)
        num1+=1
    if(len(max_valid)==0 or initial==num2):
        return(max_num)
    else:
        return(max(max_valid))
 

#Provide different values for num1 and num2 and test your program.
max_num=find_max(3,30)
print(max_num)