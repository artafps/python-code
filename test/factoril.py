def factorile(y,sum=1):
    x = sum*y
    if(y==1):
        return x 
    else:
       return factorile(y-1,x)
def factorile2(y):
    if(y==1):
        return 1 
    else:
       return factorile2(y-1) * y



print(factorile(6))

