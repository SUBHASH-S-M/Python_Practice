# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the n 
# types listed above. Iterate through each command in order and perform the corresponding operation on your list.
if __name__ == '__main__':
    N = int(input())
    l=[]
    
    for i in range(N):
        string=input()
        string=string.split(" ")
        
        if(string[0]=="insert"):
            l.insert(int(string[1]),int(string[2]))
        if(string[0]=="append"):
            l.append(int(string[1]))
        if(string[0]=="remove"):
            l.remove(int(string[1]))
        if(string[0]=="sort"):
            l.sort()
        if(string[0]=="reverse"):
            l.reverse()
        if(string[0]=="pop"):
            l.pop()
        if(string[0]=="print"):
            print(l)
          


              
                            
        
