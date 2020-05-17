import math

A, B, H, M = map(int, input().split(' '))

#print(A, B, H, M)

# c²=a²+b²−2abcosΘ

# 角度さえ求まればいける
# Aは1分で0.5度づつ
# Bは1分で6度づつ
# AとBのどっちが左側にあるかもポイント

angle_a = (H * 30) + (M * 0.5)
angle_b = M * 6

#print("angle_a", angle_a)
#print("angle_b", angle_b)

cos = 0
ret = 0

if(angle_a == angle_b):
  #print("ぴったり")
  ret = abs(A - B)
else:
  if(angle_a > angle_b):
    cos = math.cos(math.radians(angle_a - angle_b))
    #print("時針のほうが先いってる", cos)
  else:
    cos = math.cos(math.radians(angle_b - angle_a))
    #print("分針のほうが先いってる", cos)
  
  ret = math.sqrt(A**2 + B**2 - 2 * A * B * cos)

print(ret)

