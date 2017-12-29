while True:
   try:
      val = input()
      num = [x for x in val.split(",") if int(x)%2!=0]
      print (",".join(num))
      break
   except ValueError:
       print("enter valid integer numbers")
