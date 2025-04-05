# A simple calculator following OOP paradigm
#!/usr/bin/env python3

class Calculator:
    def __init__(self):
        pass

    def adder(self, x, y): # User can input two numbers to be added
        return x + y
    
    def subtracter(self, x, y): # User can input two nunmbers. Second number is always subtracted from first.
        return x-y

    def multiplicator(self, x, y):
        return x*y
    
    def divider(self, x, y):
        return x/y
        

# Adding numbers with each other
computations = Calculator()
adding = computations.adder(3,4)
print(adding) # Output 7

# Subtracting a number from another
subtracting = computations.subtracter(5,5)
print(subtracting) # Output: 0

# Multiplying a number with another
multiplication = computations.multiplicator(2,8)
print(multiplication) # Output: 16

# Dividing a number with another
division = computations.divider(2,4)
print(division) # Output: 0.5

