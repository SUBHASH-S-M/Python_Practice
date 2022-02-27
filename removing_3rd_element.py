def remove_nums(int_list):
  #list starts with 0 index
  position =3-1
  idx = 0
  len_list = (len(int_list))
  while len_list>0:
    
    idx = (position+idx)%len_list
    #print(idx)
    print(position,idx,len_list)
    #print(int_list.pop(idx))
    len_list -= 1
#n= int(input())
#l1 = []
#for i in range (0,n):
 #   ele = int(input())
 #   l1.append(ele)
nums = [10,20,30,40,50,60,70,80,90]
remove_nums(nums)
