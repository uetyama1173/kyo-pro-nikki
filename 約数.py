N = 105
ans = 0
for i in range(1,N+1):
  #約数
  c=0
  
  if i%2==1:
    for j in range(1,N+1):
        print(j)
        if i%j==0:
            c+=1
    if c==8:
      ans+=1
print(ans)  