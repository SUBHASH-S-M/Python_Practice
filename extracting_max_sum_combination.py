s="121"
from itertools import permutations 
a=permutations(s,3)
#y=[i for i in a]
y=[int("".join(i)) for i in a]
print(y)
print(max(y))
print(len(set(y)))