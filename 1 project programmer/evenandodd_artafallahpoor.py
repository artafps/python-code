number = int(input())

def numberSeparate(num):
    x=num
    arry = []
    while(x/10>0):
        arry.append(x%10)
        x = int(x/10)
    return arry

def CheckEvenOrOdd(num):
    arry_s_n = numberSeparate(num)
    for i in range(0,len(arry_s_n),2):
        if(arry_s_n[i]%2!=0):
            return "no"
    return "yes"



print(CheckEvenOrOdd(number))
