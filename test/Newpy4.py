def name(a) :
   L=[1,3, 5,7,9] 
   if (a//10 == 0):
       for i in L :
            
           if i == a:
              return 1
       return 0
   for i in L:
       if i == a%10:
           return name(a//10)+1 
   return name(a//10) 
