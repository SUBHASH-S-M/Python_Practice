#swapping the adjacent characters in the given string if the string is odd the last char is left out
s=str(input("Enter the string : "))
temp_list=list(s)
for i in range(0,len(temp_list)-1,2):
    temp_list[i],temp_list[i+1]=temp_list[i+1],temp_list[i]

s="".join(temp_list) #joinning the list to make as a string
print("The swapped string is :",s)
    