
#sort list
def sortList(L):
    lista=[]
    for i in range(len(L)):
        min_index = L[i]
        index=0
        for j in range(i+1,len(L)):
            if L[j] < min_index:
                min_index =  L[j]
                index = j
        lista.append(min_index)
        L[index]= L[i] 
    return lista
#searchbinery
def sbinery2(L,num):
    lsorting= sortList(L)
    index =(len(lsorting)//2)
    print(lsorting)
    
    if(lsorting[index]==num):
        return index
    if(len(lsorting)==1):
        return -1
    elif(lsorting[index]<num):
        result = funcreturn(lsorting[index:len(lsorting)+1],num)
        if(result == -1):
            return -1
        return result+index
    elif(lsorting[index]>num):
        result = funcreturn(lsorting[:index],num)
        if(result == -1):
            return -1
        return result
#search in list
def searchInList(L,num):
    place=[]
    for i in range(len(L)):
        if(L[i]==num):
            place.append(i)
    return place        

#quick sort
def quicksort(List):
    if(len(List)<=1):
        return List
    center=len(List)//2
    list1=list([i for i in List if i<List[center]])
    list2=list([i for i in List if i==List[center]])
    list3=list([i for i in List if i>List[center]])
    l1=quicksort(list1)
    l3=quicksort(list3)
    return l1+list2+l3

#search binery
def sbinery (L,m):
    Rlist= quicksort(L)
    n = len(Rlist)//2
    if m == Rlist[n]:
        return n
    if(len(L)==1):
        if m == Rlist[0]:
            return 0
        return -1
    if (Rlist[n]<m):
        res = sbinery(Rlist[n:len(L)+1],m)
        if res == -1:
            return -1
        return res + n
    if (Rlist[n]>m):
        res = sbinery(Rlist[:n],m)
        if res == -1:
            return -1
        return res



#macos list
def mlist(L,m=[]):
    newlist=m
    if len(L)==0:
        return m
    newlist.append(L[-1])
    mlist(L[:len(L)-1],newlist)
    return newlist


#listcheck big num
def listcheck(L):
    maxlist= L[0]
    for i in range(len(L)):
        if(L[i]>maxlist):
            maxlist = L[i]
    return maxlist

#teadad adad 
def func(a):
    if(a//10==0):
        return 1
    return func(a//10)+1

#game adad
def func2(a):
    if(a//10==0):
        return a
    return func(a//10)+a%10


#tedad adad
def func3(a):
    x = 1
    y = a
    boolean = True
    while y//10 > 0:
        y //= 10
        x += 1
    return x


#game adad
def func4(a):
    num = func3(a)
    x = 0
    y = a
    for i in range(num):
        x += y%10
        y //= 10
        
    return x



# Python code to demonstrate naive 
# method to compute gcd ( recursion ) 
def hcfnaive(a,b): 
    if(b==0): 
        return a 
    else: 
        return hcfnaive(b,a%b)

# Python code to demonstrate naive 
# method to compute gcd ( Loops )
def computeGCD(x, y): 
    if x > y: 
        small = y 
    else: 
        small = x 
    for i in range(1, small+1): 
        if((x % i == 0) and (y % i == 0)): 
            gcd = i     
    return gcd 

# Python code to demonstrate naive 
# method to compute gcd ( Euclidean algo ) 
def computeGCD(x, y): 
   while(y): 
       x, y = y, x % y 
   return x 










