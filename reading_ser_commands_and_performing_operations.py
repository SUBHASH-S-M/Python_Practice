n = int(input())
s = set(map(int, input().split()))
n2=int(input())
for i in range(n2):
    string_input=input().split(" ")
    if(string_input[0]=="pop"):
        s.pop()
    if(string_input[0]=="remove"):
        s.remove(int(string_input[1]))
    if(string_input[0]=="discard"):
        s.discard(int(string_input[1]))
print(list(s))
