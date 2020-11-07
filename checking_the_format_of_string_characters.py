'''
output Format

In the first line, print True if  input string has any alphanumeric characters. Otherwise, print False.
In the second line, print True if input string  has any alphabetical characters. Otherwise, print False.
In the third line, print True if input string  has any digits. Otherwise, print False.
In the fourth line, print True if input string  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  input string has any uppercase characters. Otherwise, print False.
'''


if __name__ == '__main__':
    s = input()
    is_upper=False
    is_lower=False
    is_alpha_numeric=False
    is_digit=False
    is_alpha=False
    
    
    for i in range(len(s)):
        if(s[i].isalnum()):
            is_alpha_numeric=True
        if(s[i].isupper()):
            is_upper=True
        if(s[i].islower()):
            is_lower=True
        if(s[i].isalpha()):
            is_alpha=True
        if(s[i].isdigit()):
            is_digit=True
    print(is_alpha_numeric)
    print(is_alpha)
    print(is_digit)
    print(is_lower)
    print(is_upper)
    
            
       
        
            