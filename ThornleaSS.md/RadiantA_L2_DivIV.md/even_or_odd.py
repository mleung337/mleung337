# Matthew Leung

# Similar to other programs as it accepts user input
# Different than other programs as it converts input to integer, and checks if input even or odd with modulo operator
# Accepts user input, assigns to number variable
number = input("Enter a number, and I'll tell you if it's even or odd: ")
# Converts number variable string to integer
number = int(number)

# Checks if number variable divisible by 2 with no remainders using modulo operator
if number %2 == 0:
    # Prints formatted message that number variable is even
    print(f"\nThe number {number} is even.")
# If number variable does not satisfy any conditions
else:
    # Prints formatted message that number variable is odd
    print(f"\nThe number {number} is odd.")
