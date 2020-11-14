
def func(k,arr):
    index=sum(arr)/k
    return(index)
def main():
    for i in range(int(input())):
        l=list(map(int,input().split(" ")))
        num=list(map(int,input().split(" ") ) )  
        num_input=func(l[1],num)
        print(int(num_input+1))

if __name__ == '__main__':
    main()
# 2 
# 6 5 
# 10 5 5 3 2 1 
# 1 1
# 100