N = 13
result = "No"
array = [1,2,3,4,5,6,7,8,9]
for i in array:
  for j in array:
    tmp = i * j
    if tmp == N:
      result = "Yes"
print(result)