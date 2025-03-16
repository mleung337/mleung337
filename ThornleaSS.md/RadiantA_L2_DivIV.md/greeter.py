# Matthew Leung

# Similar to other programs as it accepts user input
# Different than other programs as it defines input string beforehand and prints user input within formatted message

# Assigns prompt string
prompt = "If you tell us who you are, we can personalize the messages you see."
# Appends another string to prompt
prompt += "\nWhat is your name? "
# Accepts user input as string, assigning it to name variable
name = input(prompt)
# Prints formatted name variable in new line with greeting
print(f"\nHello, {name}!")
