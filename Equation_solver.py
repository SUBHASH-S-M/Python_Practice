def poly(L, x_0):
    psum = 0
    n = len(L)
    for i in range(n):
        psum = psum + L[i] * (x_0 ** i)
    return psum
def poly_zeros(L, a, b):
    zeros = []
    for x in range(a, b + 1):
        if poly(L, x) == 0:
            zeros.append(x)
    return zeros
l=[1,-4,-18,52,101,-144,-180]

a=0 
b=4 

print(poly_zeros(l,a,b))