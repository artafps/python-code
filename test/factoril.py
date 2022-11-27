def factorile(y,sum=1):
    x = sum*y
    if(y==1):
        return x 
    else:
       return factorile(y-1,x)



print(factorile(185))
