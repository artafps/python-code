list1rom =["I","II","III","IV","V","VI","VII","VIII","IX"]
n = int(input())
def func1(x):
    x1 =x
    reshte=""
    while x1:
        index =(x1%10)-1
        a = list1rom[index]
        reshte += a
        x1//=10
        
    return reshte

def macosadad(x):
    x1 = x
    reshte=""
    while x1:
        reshte += str(x1%10)
        x1 //= 10
    return int(reshte)

V=0
I=0
for i in func1(macosadad(n)):
    if(i=="I"):
        I+=1
    if(i=="V"):
        V+=1
print(func1(macosadad(n)))
print(I*V)
