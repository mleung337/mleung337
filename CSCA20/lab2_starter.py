# Matthew Leung

# All user input (save for position guesses) will be put through casefold method from str class to make all letters lowercase

#prompt the trainer for the passcode
passcode = str.casefold(input("Trainer: enter 5 letter passcode: "))
#print a bunch of empty lines so that the entered passcode scrolls off the screen
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

####ROUND 1#####
print("Round 1: Guess 5 letters to see if they're in the passcode ")
#do this 5 times... later when we learn about loops, we can come back and make
#this a lot simpler
# Creates list to store bool values
tf_guesses = []
# for loop  that lets the user to make a guess then immediately stores bool in list
for i in range(5):
    guess = str.casefold(input("Guess #" + str(i + 1) + ": letter to check: "))
    tf_guesses.append(guess in passcode)
# for loop that prints the bool value for each guess
for i in range(5):
    print(tf_guesses[i])

#####ROUND 2#####
print("Round 2: Guess 5 letter/position combinations to see if you have them correct")
# Creates list to store bool values
tf_guesses_v2 = []
# for loop that lets user to make a guess for letter and position and immediately stores bool in list
for i in range(5):
    letter_guess = str.casefold(input("Guess #" + str(i + 1) + ": letter to check: "))
    position_guess = int(input("Guess #" + str(i + 1) + ": position to check: "))
    tf_guesses_v2.append(passcode[position_guess - 1] == letter_guess)
# for loop that prints the bool value for each guess
for i in range(5):
    print(tf_guesses_v2[i])

#####ROUND 3#####
print("Round 3: Guess the whole word, and I'll tell you if it's correct")
# counter for while loop solely for the number of times guessed
counter = 1
# while loop that lets the user guess then prints bool value; if user guesses correctly, program ends
while True:
    guess = str.casefold(input("Guess #" + str(counter) + ": guess the passcode: "))
    print(guess == passcode)
    counter += 1
    if guess == passcode:
        raise SystemExit
        
    

