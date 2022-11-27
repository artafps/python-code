def isprime(n):
    new_n = n//2
    for i in range(2,new_n+1):
        if n%i == 0:
            return False
    return True


def checkthelist(L):
    new_list = [i for i in L if isprime(i)]
    return new_list

print(checkthelist([1,2,3,4,5,6,2,1,12,13,14,25,23,21,19]))
    
