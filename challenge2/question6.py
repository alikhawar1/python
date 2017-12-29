import sys
while True:
   try:
      val=[x for x in input().split(',')]
      val.sort()
      print(','.join(val))
      break
   except EOFError:
        print("please enter compareable values")
