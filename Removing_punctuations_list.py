punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "Hello!!!, he said ---and went."
punctuations=list(punctuations)
final_str=[]
for  i in my_str:
    if(i in punctuations):
        pass
    else:
        final_str.append(i)
final_str="".join(final_str)
print(final_str) 