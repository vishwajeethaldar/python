# import specific function
from functions import square
# Import entire module
import functions 

n = int(input("Number: "))

for i in range(n):
    sqr = functions.square(i)
    print(f"square of {i} is {sqr}.")

