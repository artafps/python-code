n = int(input())

def harmonic(num):
    if (num == 1):
        return 1
    else:
        return harmonic(num-1)+(1/num)

print(harmonic(n))
