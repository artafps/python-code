n= int(input())
def createEquilateralTriangle(x):
    for i in range(0,x):
        print(i*"* ")
    for j in range(x,0,-1):
        print(j*"* ")
createEquilateralTriangle(n)



