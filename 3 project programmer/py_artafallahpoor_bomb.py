n = input().split(" ")

bombMap = []

for i in range(int(n[0])):
    bombMap.append(list(range(0,int(n[1]))))

k = int(input())
zogmoratab = []
for i in range(k):
    z = input().split(" ")
    zogmoratab.append(z)


for i in zogmoratab:
    x=int(i[0])-1
    y=int(i[1])-1
    bombMap[x][y]= "*"


for i in range(len(bombMap)):
    for j in range(len(bombMap[i])):
        if bombMap[i][j] != "*":
            bombMap[i][j] = 0


for i in range(len(bombMap)):
    for j in range(len(bombMap[i])):
        if bombMap[i][j] == "*":
             if(i>0 and j>0 and i<(len(bombMap)-1) and j<(len(bombMap[i])-1)):
                if(bombMap[i-1][j-1] != "*"):
                    bombMap[i-1][j-1]+=1
                if(bombMap[i][j-1] != "*"):
                    bombMap[i][j-1]+=1
                if(bombMap[i-1][j] != "*"):
                    bombMap[i-1][j]+=1
                if( bombMap[i+1][j+1] != "*"):
                    bombMap[i+1][j+1]+=1
                if(bombMap[i][j+1] != "*"):
                    bombMap[i][j+1]+=1
                if(bombMap[i+1][j] != "*"):
                    bombMap[i+1][j]+=1
                if(bombMap[i+1][j-1] != "*"):
                    bombMap[i+1][j-1]+=1
                if(bombMap[i-1][j+1] != "*"):
                    bombMap[i-1][j+1]+=1
             if(i>0 and j==0 and i<len(bombMap)-1):  
                if(bombMap[i-1][j] != "*"):
                    bombMap[i-1][j]+=1
                if( bombMap[i+1][j+1] != "*"):
                    bombMap[i+1][j+1]+=1
                if(bombMap[i][j+1] != "*"):
                    bombMap[i][j+1]+=1
                if(bombMap[i+1][j] != "*"):
                    bombMap[i+1][j]+=1
                if(bombMap[i-1][j+1] != "*"):
                    bombMap[i-1][j+1]+=1
             if(i==0 and j>0 and j<len(bombMap[i])-1 ):
                if(bombMap[i][j-1] != "*"):
                    bombMap[i][j-1]+=1
                if( bombMap[i+1][j+1] != "*"):
                    bombMap[i+1][j+1]+=1
                if(bombMap[i][j+1] != "*"):
                    bombMap[i][j+1]+=1
                if(bombMap[i+1][j] != "*"):
                    bombMap[i+1][j]+=1
                if(bombMap[i+1][j-1] != "*"):
                    bombMap[i+1][j-1]+=1

             if(i>0 and j==len(bombMap[i])-1 and i<len(bombMap)-1):  
                if(bombMap[i-1][j] != "*"):
                    bombMap[i-1][j]+=1
                if( bombMap[i+1][j] != "*"):
                    bombMap[i+1][j]+=1
                    
                if(bombMap[i-1][j-1] != "*"):
                    bombMap[i-1][j-1]+=1
                if(bombMap[i+1][j-1] != "*"):
                    bombMap[i+1][j-1]+=1
                if(bombMap[i][j-1] != "*"):
                    bombMap[i][j-1]+=1
             if(i==len(bombMap)-1 and j>0 and j<len(bombMap[i])-1 ):
                if(bombMap[i][j+1] != "*"):
                    bombMap[i][j+1]+=1
                if( bombMap[i][j-1] != "*"):
                    bombMap[i][j-1]+=1
                if(bombMap[i-1][j+1] != "*"):
                    bombMap[i-1][j+1]+=1
                if(bombMap[i-1][j-1] != "*"):
                    bombMap[i-1][j-1]+=1
                if(bombMap[i-1][j] != "*"):
                    bombMap[i-1][j]+=1
             if(i==0 and j==0):  
                if(bombMap[i+1][j+1] != "*"):
                    bombMap[i+1][j+1]+=1
                if(bombMap[i][j+1] != "*"):
                    bombMap[i][j+1]+=1
                if(bombMap[i+1][j] != "*"):
                    bombMap[i+1][j]+=1
             if(i==len(bombMap)-1 and j==len(bombMap[i])-1):  
                if(bombMap[i-1][j-1] != "*"):
                    bombMap[i-1][j-1]+=1
                if(bombMap[i][j-1] != "*"):
                    bombMap[i][j-1]+=1
                if(bombMap[i-1][j] != "*"):
                    bombMap[i-1][j]+=1
             if(i==len(bombMap)-1 and j==0):
                if( bombMap[i-1][j+1] != "*"):
                    bombMap[i-1][j+1]+=1
                if(bombMap[i][j+1] != "*"):
                    bombMap[i][j+1]+=1
                if(bombMap[i-1][j] != "*"):
                    bombMap[i-1][j]+=1
             if(i==0 and j==len(bombMap[i])-1):
                if( bombMap[i][j-1] != "*"):
                    bombMap[i][j-1] +=1
                if(bombMap[i+1][j-1] != "*"):
                    bombMap[i+1][j-1]+=1
                if(bombMap[i+1][j] != "*"):
                    bombMap[i+1][j]+=1
               
for i in bombMap:
    for j in i: 
        print(j , end = " ")
    print(" ")
