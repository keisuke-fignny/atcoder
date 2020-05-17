K = int(input())
S = str(input())

# print(K, S)

if(len(S) <= K):
  print(S)
else:
  print(S[:K] + "...")

