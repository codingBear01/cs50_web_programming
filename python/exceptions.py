import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid Input.")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)
    # sys.exit means exit the program with a status code of one(something went wrong in this program)

print(f"{x} / {y} = {result}")
