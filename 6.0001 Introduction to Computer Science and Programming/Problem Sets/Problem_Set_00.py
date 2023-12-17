# # This function will find the log to base 2. If it can not do it perfectly, it'll go into a loop forever. Not ideal.  
# # Regardless, it was fun to make, but not very useful 
# def log_2(x):
#     h = 0
#     base = 2
#     number = 0
#     x = int(x) # Convert input to integer
#     while h != x:
#         number += 1
#         h = base ** number

#     return number

# logarithmic = str(log_2(x))
# print("log(x) = ", logarithmic, "\n")


"""
Problem Set 0

Write a program that does the following in order:
    - Asks the user to enter a number "x"
    - Asks the user to enter a number "y"
    - Prints out number "x", raised to the power "y".
    - Print out the log (base 2) of "x"
"""
import numpy

x = input("\nEnter a number x: ")
y = input("Enter a number y: ")

x = int(x) # Convert string to int
y = int(y) # Convert string to int

print("x**y = ", str(x ** y))
print("log(x) = ", numpy.log2(x)) 
