# Problem Set 0

### Christopher A. Nelson - November 22, 2023

Write a program that does the following in order:

1. Asks the user to enter a number “x”
2. Asks the user to enter a number “y”
3. Prints out number “x”, raised to the power “y”.
4. Prints out the log (base 2) of “x”.

```python
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


```

```bash
Enter a number x: 2
Enter a number y: 3
x**y =  8
log(x) =  1.0
```


