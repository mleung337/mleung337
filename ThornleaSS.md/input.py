# Matthew Leung

while True:
    a = int(input("Enter an integer for variable a. "))
    b = int(input("Enter an integer for variable b. "))
    print("The sum of variables a and b is", a + b, ".")
    question = input("Try again? (y/n)")
    if 'y' in question:
        continue
    elif 'n' in question:
        print("Goodbye.")
        break
    else:
        print("Invalid input.")
