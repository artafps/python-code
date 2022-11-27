n = int(input())
m = int(input())
if(m<n):
    a=n
    n=m
    m=a
def fibanachi(x):
    arryfib = [1]
    a=0
    b=1
    
    for i in range(x):
        arryfib.append(b)
        c=a+b
        a=b
        b=c
        
    return arryfib
def selectPartOfTheDomain(x,y):
    arryfib = fibanachi(y)
    for i in range(1,len(arryfib)):
        if(i>=x):
            print(arryfib[i]) 
selectPartOfTheDomain(n,m)
