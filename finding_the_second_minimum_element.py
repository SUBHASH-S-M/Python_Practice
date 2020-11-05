if __name__ == '__main__':
    dict1={}
    min1=1000
    min2=1000
    l=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        dict1[name]=score
        
        if(score<min1):
            min2=min1
            min1=score
        elif(score>min1 and score<min2):
            min2=score
        else:
            pass
    for x, y in dict1.items():
        if(y==min2):
            l.append(x)
    for i in sorted(l):
        print(i)