A = str(input())

digit_right = A[len(A)-1]

if(digit_right in ('2','4','5','7','9') ):
  print("hon")
elif(digit_right in ('0','1','6','8')):
  print("pon")
else:
  print("bon")

