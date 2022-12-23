M =101

N=4
int =[10,8,8,6]

#0の値を101個生成している
#0の値も含まれるので+1 
exist= [0]*101

for i in range(N):
    d = int[i]
    exist[d] = 1

print(exist[100])
print(sum(exist))
