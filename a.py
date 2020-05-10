S = input()
T = input()

T_minus_1 = T[:len(S)]

if(T_minus_1 == S):
  print("Yes")
else:
  print("No")

