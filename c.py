def count_up(idx_list, lv_list):
#  print(idx_list, "の組み合わせのカウントアップ")
  new_lv_list = []
  for j in range(M):
    each_total_lv = 0
    for i in idx_list:
      each_total_lv += lv_list[i][j]
#      print(each_total_lv)
      if(each_total_lv >= X):
#        print(j, "番地の能力は達成")
        break
    if(each_total_lv < X):
#      print(idx_list, "だと未達成。次")
      return -1
  
  price = 0;
  for a in idx_list:
    price += prices[a]
  
#  print("idx_list=", idx_list, "金額は", price)
  
  return price
    
  

from itertools import combinations

N,M,X = map(int, input().split(' '))

prices = []
lv_ups = []
max_price = 0

# i = 0から
for i in range(N):
  tmp = tuple(map(int, input().split(' ')))
  max_price += tmp[0]
  prices.append(tmp[0])
  lv_ups.append(tmp[1:len(tmp)])

#print("最大金額=", max_price)

all_read = []
complete = True
for j in range(M):
    each_total_lv = 0
    for i in range(len(lv_ups)):
      each_total_lv += lv_ups[i][j]
    
    if (each_total_lv < X):
      complete = False
    all_read.append(each_total_lv)
    
    
# 判定
if(complete):
  for z in reversed(range(1, N)):
    comb = combinations(range(N), z)
    for e in comb:
      counted_price = count_up(e, lv_ups)
      if(counted_price > 0 and max_price > counted_price):
        max_price = counted_price
  
  print(max_price)
  
else:
  print(-1)

