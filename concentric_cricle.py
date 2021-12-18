def processCircles(circles,n1,n2):
    circles.sort()
    r1=circles[n1-1]
    circles.sort(reverse=True)
    r2=circles[n2-1]
    r1+=1 
    r2+=1
    print(r1,r2)
    val=(3.14*r2*r2)-(3.14*r1*r1)
    return int(val)
    
    
print(processCircles([4,5,5,0,6,3,9],3,3))