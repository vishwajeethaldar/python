import sys

try :
    x = int(input("X: "))
    y = int(input("Y: "))
except ValueError :
    print("Error: Invalid Input")
    sys.exit(1)
try :
    result = x/y
except ZeroDivisionError :
    print("Error: Cannot Devide by Zero")
    sys.exit(1)

print(f"division of {x}/{y}  is =  {result}")