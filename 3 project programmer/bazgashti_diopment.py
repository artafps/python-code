def listo(l,n=1,m=1):
    if len(l)%2 != 0:
        x=len(l)//2
        if(len(l)<1):
            return True
        if(n!=m):
            return False
        return listo(l[0:x-1]+l[x+2:len(l)],l[x-1],l[x+1])
    else:
        x=len(l)//2-1
        if(len(l)<1):
            return True
        if(n!=m):
            return False
        return listo(l[0:x]+l[x+2:len(l)],l[x],l[x+1]) 

print(listo([5, 4, 1, 2, 3, 2, 1, 4, 5]))
