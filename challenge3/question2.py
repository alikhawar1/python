while True:
   try:
      a=input()
      letters=0
      digits=0
      for x in a:
        if x.isdigit():
           digits = digits + 1
        elif x.isalpha():
             letters=letters + 1
        else:
             print("values are not entered properly")

      print ("Letters" ,letters)
      print ("Digits" ,digits)
      break
   except ValueError:
       print("enter valid integer numbers and letters")

