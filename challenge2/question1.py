import sys
import math
while True:
    try:
        print( "enter number")
        num= float (input())
        print(math.sqrt(num))

        break
    except ValueError:
        print ("enter a valid value")

