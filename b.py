A_1, B_0, C_minus1, K = map(int, input().split(' '))

max_total = 0

if(K <= A_1):
  max_total = K
elif(K > A_1 and K <= (A_1 + B_0)):
  max_total = A_1
else:
  left = K - (A_1 + B_0)
  if(left <= C_minus1):
    max_total = A_1 - left
  else:
    max_total = A_1 - C_minus1
  
print(max_total)

