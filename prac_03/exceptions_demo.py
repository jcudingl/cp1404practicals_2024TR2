"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When input invalid literal for int().
2. When will a ZeroDivisionError occur?
When denominator is 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
To add an error check for denominator: if the input is 0, return invalid input and ask for a new input.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    # Error check added
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")