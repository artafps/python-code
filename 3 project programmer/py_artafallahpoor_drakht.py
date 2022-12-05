n = input().split(" ")


def func2(a):
    listadad = []
    x= a
    for i in range(len(a)):
        listadad.append(x[i])
    return listadad

if(len(n)%2==1):
    x= n
    z=0    
    list2= list(range(len(x)))
    for i in range(0,len(x)):
        j= i*2
        if(j<len(x)):
            list2[j]= x[i]
            z=i+1
    xnum =len(n)-2
    for i in range(z,len(x)):
        if (xnum<len(x) and 0<xnum ):
            list2[xnum]= x[i]
            xnum = xnum-2
    for i in list2:
        print(i ,end=" ")
else:
    x=n
    z=0    
    list2= list(range(len(x)))
    for i in range(0,len(x)):
        j= i*2
        if(j<len(x)):
            list2[j]= x[i]
            z=i+1
    xnum =len(n)-1
    for i in range(z,len(x)):
        if (xnum<len(x) and 0<xnum ):
            list2[xnum]= x[i]
            xnum = xnum-2
    for i in list2:
        print(i ,end=" ")



