def second_max(arr):
  """
  function returns the 1st max,2nd max value in the array
  """
  #for calcualting max we need (min-1) value in the  range of array assuming the the value which is not possible
  lar1=-10000000000000000000000000000000 
  lar2=-1000000000000000000000000000000
  nunique=len(set(arr))  #checking length of unique numbers
  if(nunique<2):
    if(len(arr)<1):
      return ["Null","Null"]
    else:
      return [arr[0],"Null"]
  else:
    try:
      for i in range(len(arr)):
        if(arr[i]>lar1):
          lar2=lar1      #Assign current max to 2nd max and  max to the max element found now
          lar1=arr[i]
        elif(arr[i]>lar2 and arr[i]<lar1):
          lar2=arr[i]
    except TypeError:
      return ("Array arguments should be of same type")
    return ([lar1,lar2])
print("Blank")
print(second_max([]))
print("Only One Ele is there")
print([1])
print(second_max([1]))
print("All are positive")
print([1,2,3,4,5,6])
print(second_max([1,2,3,4,5,6]))
print("Positive and same")
print([1,1])
print(second_max([1,1]))
print("all are negative")
print([-1,-2,-3,-4,-5,-6])
print(second_max([-1,-2,-3,-4,-5,-6]))
print("negative and same")
print([-11,-11])
print(second_max([-11,-11]))
print("Both negative and positive")
print([-1,-2,-3,-4,-5,6])
print(second_max([-1,-2,-3,-4,-5,6]))
print("Array of diff dataypes which is uncomaprable")
print(second_max([1,2,-1,3,"Subhash",-5]))

 