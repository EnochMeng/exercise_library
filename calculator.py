import re
brackets=re.compile(r'(?<=\()[^()]+(?=\))')

mul=re.compile(r'(\d+\.*\d*)(\*)(\d\.*\d*)')
div=re.compile(r'(\d\.*\d*)(\/)(\d\.*\d*)')
add=re.compile(r'(\d\.*\d*)(\+)(\d\.*\d*)')
sub=re.compile(r'(\d\.*\d*)(\-)(\d\.*\d*)')

s=r'2*8*2'
def excute_mul(s):
    s.replace(' ','')
    print(s)
    while True:
        if mul.search(s) != None:
            a=float(mul.search(s).group(1))
            b=float(mul.search(s).group(3))
            result=a*b
            result=str(result)
            s=s.replace(mul.search(s).group(0),result)
            print(s)
        else:
            break
    return s

        
        
    


