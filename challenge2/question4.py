import sys
import math
while True:
   try:
      c=50
      h=30
      num=[]
      x=[i for i in input().split(',')]
      for d in x:
         num.append(str(int(math.sqrt((2*c*float(d)/h)))))
      print(','.join(num))
      break
   except ValueError:
       print("enter valid integer numbers")
