
a=input()
upper=0
lower=0
for c in a:
    if c.isupper():
        upper=upper + 1
    elif c.islower():
          lower=lower + 1
    else:
        print("enter only alphabatic string")
print ("upper letters are" ,upper)
print ("lower letters are" ,lower)
