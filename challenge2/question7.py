val = []
for x in range(1000, 3001):
    s = str(x)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        val.append(s)
print (",".join(val))
