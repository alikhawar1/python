import sys
while True:
   try:
       rown = int(input('rows:'))
       coln = int(input('columns:'))
       multilist = [[0 for col in range(coln)] for row in range(rown)]
       print(multilist)

       multilist= [[i*j for i in range(rown)] for j in range(coln)]
#for row in range(rown):
#    for col in range(coln):
#        multilist[row][col]= row*col

       print(multilist)
       break
   except Exception:
       print ("enter a integer value for  rows and coloumn")
