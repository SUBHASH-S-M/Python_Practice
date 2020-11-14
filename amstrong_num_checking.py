'''
Write a Python function to find all the Strong numbers in a given list of numbers.
Write another function to find and return the factorial of a number. Use it to solve the problem.

Example:
A number is considered to be a Strong number if sum of the factorial of its digits is equal to the number itself.
145 is a Strong number as 1! + 4! + 5! = 145.
'''

#PF-Exer-26

def factorial(number):
     #remove pass and write your logic to find and return the factorial of given number
    import math as mt 
    return(mt.factorial(number))
    
def find_strong_numbers(num_list):
     #remove pass and write your logic to find and return the list of strong numbers from the given list
     re=[]
     for i in num_list:
         l=list(str(i))
         l=list(map(int,l))
         sum=0
         for j in l:
             sum+=factorial(j)
         if(sum==i):
            re.append(i)
     return(re)

num_list=[145,375,100,2,10]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)