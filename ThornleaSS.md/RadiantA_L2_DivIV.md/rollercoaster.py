# Matthew Leung

# Similar to other programs as accepts user input
# Different than other programs as it converts input to integer, and checks if input is a certain value or above

# Accepts user input as string, assigns to height variable
height = input("How tall are you in inches?")
# Converts height variable from string to integer
height = int(height)

# Checks if height variable equal or greater than 48
if height >= 48:
    # Prints message that user is tall enough
    print("\nYou're tall enough to ride!")
    
# If height variable does not satisfy any conditions
else:
    # Prints message that user is needs to be older
    print("\nYou'll be able to ride when you're a little older.")
