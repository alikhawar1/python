import re
pas= input("enter your password")
i = True
while i:  
    if (len(pas)<6 or len(pas)>12):
        break
    elif not re.search("[a-z]",pas):
        break
    elif not re.search("[0-9]",pas):
        break
    elif not re.search("[A-Z]",pas):
        break
    elif not re.search("[$#@]",pas):
        break
    elif re.search("\s",pas):
        break
    else:
        print("Valid Password")
        i=False
        break

if i:
    print("enter a valid password")
