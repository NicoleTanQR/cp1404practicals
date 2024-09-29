"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When argument value is inappropriate like a string not representing
an integer being given to int()
2. When will a ZeroDivisionError occur?
When second argument to division or modulo operation is zero like
denominator for division in this case
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator must not be zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
