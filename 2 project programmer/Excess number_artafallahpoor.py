n = input()

def numberExtraction(num):
    sum_of_ext_n=0
    for i in range(len(n)):
        for j in range(10):
            if(num[i]==str(j)):
                sum_of_ext_n += j
    return sum_of_ext_n
        
def checkAbundantNumber(num):
    sum_num=0
    for i in range(1, num):
         if num % i == 0:
            sum_num+=i
         if(num<sum_num):
            return True
    return False
    
if(checkAbundantNumber(numberExtraction(n))):
    print("Is an Abundant Number")
else:
    print("Is not an Abundant Number")

