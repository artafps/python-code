n = int(input())
list_check_tom = []
for i in range(n):
    list_check_tom.append(int(input()))



def checkTomNumber(num):
    sum_num=0
    for i in range(1,num):
        if(sum_num==num):
            return True
        if(sum_num>num):
            return False
        print(i,sum_num)
        sum_num+=i

for i in list_check_tom:
    print(checkTomNumber(i))

        

