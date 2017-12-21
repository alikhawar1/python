str_list = [str(x) for x in range(1000,3001)]
val = [x for x in str_list if ((int(x[0])%2==0) and (int(x[1])%2==0) and (int(x[2])%2==0) and (int(x[3])%2==0))]
#for x in eval(str(range(1,20))):
#  print(x)
#for x in range(1000, 3001):
#    s = str(x)
#    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
#        val.append(s)
print (",".join(val))
