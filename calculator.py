import re

def mul_div(s):
    while re.findall(r'\d+\.?\d*[*/]\d+\.?\d*',s):
        s1=re.search(r'\d+\.?\d*[*/]\d+\.?\d*',s).group()
        if re.findall(r'[*]',s1):
            x,y=re.split(r'[*]',s1)
            x=float(x)
            y=float(y)
            s2=x*y
            s2=str(s2)
            s=s.replace(s1,s2)
        else:
            x,y=re.split(r'[/]',s1)
            x=float(x)
            y=float(y)
            s2=x/y
            s2=str(s2)
            s=s.replace(s1,s2)
    return s

def add_sub(s):
    while re.findall(r'\d+\.?\d*[+-]\d+\.?\d*',s):
        s1=re.search(r'\d+\.?\d*[+-]\d+\.?\d*',s).group()
        if re.findall(r'[+]',s1):
            x,y=re.split(r'[+]',s1)
            x=float(x)
            y=float(y)
            s2=x+y
            s2=str(s2)
            s=s.replace(s1,s2)
        else:
            x,y=re.split(r'[-]',s1)
            x=float(x)
            y=float(y)
            s2=x-y
            s2=str(s2)
            s=s.replace(s1,s2)
    return s

def check_str(s):
    flag=True
    if re.findall(r'[^0-9/*\-+()\.]',s):
##        print('invalid data')
        flag=False
    else:
        print('valid data')
    return flag

def format_str(s):
    s=s.replace(' ','')
    s=s.replace('++','+')
    s=s.replace('-+','-')
    
    s=s.replace('+-','-')
    s=s.replace('--','+')
    
    s=s.replace('*/','*')
    s=s.replace('/*','/')
    
    s=s.replace('**','*')
    s=s.replace('//','/')
    
    return s

string=input('pls enter your data to calculate:')
string=format_str(string)
if check_str(string):
    
    while re.findall(r'\(',string):
        string_brackets=re.search(r'\([^()]+\)',string).group()
        string_brackets0=string_brackets[1:-1]
##        print(string_brackets0)
        string_brackets1=mul_div(string_brackets0)
##        print(string_brackets1)
        string_brackets2=add_sub(string_brackets1)
##        print(string_brackets2)
        string=string.replace(string_brackets,string_brackets2)
##        print(string)
    else:
        string1=mul_div(string)
##        print(string1)
        string2=add_sub(string1)
    
    print(string2)
else:
    print('invalid data')


        
        
    


